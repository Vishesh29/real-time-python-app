from translate import Translator
import sys

def translate_file(input_file, output_file, target_language='ja'):
    """
    Translates the content of the input file to the specified target language
    and writes the translation to the output file.

    Parameters:
    input_file (str): Path to the input text file.
    output_file (str): Path to the output text file.
    target_language (str): Target language for translation (default is 'ja' for Japanese).
    """
    translator = Translator(to_lang=target_language)
    try:
        with open(input_file, mode='r', encoding='utf-8') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            with open(output_file, mode='w', encoding='utf-8') as files:
                files.write(translation)
            print(f'Translation completed and saved to {output_file}')
    except IOError as e:
        print(f'I/O Error: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    translate_file(input_file, output_file)