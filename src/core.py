from openai import *
from src.tools import *

def translate_text(api_config, original, target_language):
    try:
        titles, chapters = split_into_chapters(original)
        messages_static = [
            {"role": "system", "content": "You are a professional literary translator. Your task is to translate a novel from one language to another. Ensure that the translation is coherent and fluent, conforming to the expression habits of the target language. Retain the original style, tone, and cultural background. Unify character names, place names, and core terminology. And only output the translation, without adding any comments or explanations."}
        ]
        cache = []
        cache_scope = 4
        translations = ""
        for index, chapter in enumerate(chapters):
            print(f"[info] Translating {titles[index]}...")
            messages = messages_static + cache
            messages.append({"role": "user", "content": f"Please translate the following novel text into fluent and idiomatic {target_language}, retaining the format and paragraph breaks. Only output the translation, without adding any comments or explanations. The text you need to translate is as follows: {chapter}"})
            cache.append(messages[-1])
            translation = call_openai_api_stream(api_config, messages, 8000)
            translation = translation.replace('\n\n', '\n')
            translations += f"{translation}\n\n\n"
            cache.append({"role": "assistant", "content": translation})
            if len(cache) > cache_scope:
                cache.pop(0)
    except Exception as e:
        print(f"[error] An unexpected error occurred: {e}")
    finally:
        return translations

def call_openai_api_stream(api_config, messages, max_tokens):
    client = OpenAI(api_key=api_config['api_key'], base_url=api_config['base_url'])
    temperature = 0.7
    if api_config['model'] == "deepseek-chat" or api_config['model'] == "deepseek-reasoner":
        temperature = 1.3
    try:
        response = client.chat.completions.create(
            model=api_config['model'],
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )
        complete_response = ""
        last_chunk = None
        for chunk in response:
            last_chunk = chunk
            if hasattr(chunk.choices[0].delta, "content"):
                content_chunk = chunk.choices[0].delta.content
                print(content_chunk, end='', flush=True)
                complete_response += content_chunk
        print()
        usage = {
            "completion_tokens": last_chunk.usage.completion_tokens,
            "prompt_tokens": last_chunk.usage.prompt_tokens,
            "total_tokens": last_chunk.usage.total_tokens
        }
        update_usage_log(usage, api_config['base_url'], api_config['model'])
        return complete_response
    except Exception as e:
        print(f"[error] API connection failed: {e}")
        return None

if __name__ == '__main__':
    pass