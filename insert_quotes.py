# Write a script that inserts quotes into strings contained in a file.
# The script should take two arguments: the name of the file to read and the name of the file to write.
# The script should read the file passed as the first argument and insert quotes around each string.
# The script should write the modified text to the file passed as the second argument.
# The script should not modify the original file.
# The script should handle the following cases:
# - Strings that contain quotes
# - Strings that contain escaped quotes
# - Strings that contain escaped backslashes
# - Strings that contain escaped backslashes and quotes
# - Strings that contain escaped backslashes, quotes, and other characters
# - Strings that contain escaped backslashes, quotes, and other characters, and are split across multiple lines
# - Strings that are separated by commas
# - Strings that are separated by commas and contain escaped backslashes, quotes, and other characters  
# - Strings that are separated by commas and contain escaped backslashes, quotes, and other characters, and are split across multiple lines
# - Strings that are separated by commas and contain escaped backslashes, quotes, and other characters, and are split across multiple lines, and are separated by commas

# Save the file as a python module with all the contents stored in a set named not_pii


# Save the file as a python module with all the contents stored in a set named not_

import sys
import re


def insert_quotes(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        text = re.sub(r'(?<!\\)"', r'\\"', text)
        text = re.sub(r'(?<!\\)\\', r'\\\\', text)
        text = re.sub(r'(?<!\\)([^\s,]+)', r'"\1"', text)
        return text


def main():
    if len(sys.argv) != 3:
        print('Usage: {} <input_file> <output_file>'.format(sys.argv[0]))
        sys.exit(1)
    with open(sys.argv[2], 'w') as f:
        f.write(insert_quotes(sys.argv[1]))


if __name__ == '__main__':
    main()
