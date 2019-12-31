# strings, bytes ad character encodings

import sys

script, input_encoding, error = sys.argv

# main function


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding,  errors)


def print_line(line, encoding, errors):
    next_language = line.strip()  # research this ****
    raw_bytes = next_language.encode(encoding, errors=errors)
    result_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, " <========> ", result_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
