import json
import os
import re
from datetime import datetime
from openai import *

# Test if API configuration is correct
def test_api_connection(base_url, api_key, model):
    client = OpenAI(api_key=api_key, base_url=base_url)
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, world!"}
            ]
        )
        print("[success] API connection successful:", completion.choices[0].message.content)
        return True
    except Exception as e:
        print(f"[error] API connection failed: {e}")
        return False

# Read JSON file and return a dictionary
def read_json_to_dict(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"[error] Failed to read JSON file: {e}")
        return None

# Save dictionary as a JSON file
def write_dict_to_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"[write] {file_path}")
    except Exception as e:
        print(f"[error] Failed to write to JSON file: {e}")

# Read TXT file and return a string
def read_txt_to_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"[error] Failed to read TXT file: {e}")
        return None

# Save string as a TXT file
def write_string_to_txt(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"[write] {file_path}")
    except Exception as e:
        print(f"[error] Failed to write to TXT file: {e}")

# Update usage information
def update_usage_log(usage, base_url, model):
    log_file_path = 'usage.log'
    if not os.path.exists(log_file_path):
        try:
            open(log_file_path, 'w').close()  # 创建空文件
        except Exception as e:
            print(f"[error] Failed to create usage.log: {e}")
            return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f'{{ "base_url": "{base_url}", "model": "{model}", "completion_tokens": {usage["completion_tokens"]}, "prompt_tokens": {usage["prompt_tokens"]}, "total_tokens": {usage["total_tokens"]}, "timestamp": "{timestamp}" }}\n'
    try:
        with open('usage.log', 'a') as file:
            file.write(log_entry)
    except Exception as e:
        print(f"[error] Failed to write to usage.log: {e}")

# Summarize text for brief display
def summarize_text(text):
    if len(text) > 500:
        return text[:500].strip().replace('\n\n', '\n') + "..."
    else:
        return text.strip().replace('\n\n', '\n')

# Split text by chapters
def split_into_chapters(text):
    chapter_title_pattern = re.compile(r'^.{0,5}第(?:[零一二三四五六七八九十百千万]+|\d+)章(.{0,30})?\n$|^Chapter\s+\d+:(.{0,30})\n$', re.MULTILINE)
    chapter_titles = []
    chapters = []
    chapter_content = ""
    lines = text.split('\n')
    for line in lines:
        line = re.sub(r'[　&]nbsp;', ' ', re.sub(r'\s+', ' ', line)).strip() + '\n'
        if not re.sub(r'\s', '', re.sub(r'[\r\n]', '', line)).strip():
            continue
        if chapter_title_pattern.match(line):
            if chapter_content:
                chapters.append(chapter_content)
            chapter_content = line + '\n'
            chapter_titles.append(line.strip())
        else:
            chapter_content += line
    if chapter_content:
        chapters.append(chapter_content)
    if len(chapter_titles) < len(chapters):
        chapter_titles.insert(0, "Other")
    return chapter_titles, chapters

# Get filename
def get_filename_without_extension(file_path):
    base_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    return file_name_without_ext

if __name__ == '__main__':
    pass