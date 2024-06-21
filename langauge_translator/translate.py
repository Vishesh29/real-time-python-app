from translate import Translator
import sys

def translate_file(input_file, output_file, source_language='en', target_language='ja'):
    """
    Translates the content of the input file from the source language to the target language
    and writes the translation to the output file.

    Parameters:
    input_file (str): Path to the input text file.
    output_file (str): Path to the output text file.
    source_language (str): Source language for translation (default is 'en' for English).
    target_language (str): Target language for translation (default is 'ja' for Japanese).
    """
    translator = Translator(from_lang=source_language, to_lang=target_language)
    try:
        with open(input_file, mode='r', encoding='utf-8') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            with open(output_file, mode='w', encoding='utf-8') as files:
                files.write(translation)
            print(f'Translation from {source_language} to {target_language} completed and saved to {output_file}')
    except IOError as e:
        print(f'I/O Error: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <output_file> [source_language] [target_language]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    source_language = sys.argv[3] if len(sys.argv) > 3 else 'en'
    target_language = sys.argv[4] if len(sys.argv) > 4 else 'ja'

    translate_file(input_file, output_file, source_language, target_language)
