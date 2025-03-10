import sys
from src.tools import *
from src.core import *

def main():
    if len(sys.argv) < 2:
        return print('Usage: python run.py "path_to_txt_file" "target_language"\nExample: python run.py "input/text.py" "english"')
    
    # Get the passed arguments
    input_file_path = sys.argv[1:][0]
    target_language = sys.argv[1:][1]
    print(f"File path: {input_file_path}")
    print(f"Target translation language: {target_language}")

    # Load global configuration
    global_config = read_json_to_dict('global_config.json')
    api_config = global_config['api_config']
    output_directory = global_config['file_paths']['output_directory']
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    print(f"Base URL: {api_config['base_url']}")
    print(f"Model: {api_config['model']}")

    # Test if API configuration is correct
    # api_connection = test_api_connection(api_config['base_url'], api_config['api_key'], api_config['model'])
    # if not api_connection:
    #     sys.exit(1)

    # Get original text
    original = read_txt_to_string(input_file_path)
    if original:
        print(f"Original: \n{summarize_text(original)}")

    # Start translation
    translations = translate_text(api_config, original, target_language)
    write_string_to_txt(translations, os.path.join(output_directory, f"{get_filename_without_extension(input_file_path)}_translated_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"))

if __name__ == '__main__':
    main()