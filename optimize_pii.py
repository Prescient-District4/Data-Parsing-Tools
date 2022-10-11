# Write a script that inserts quotes into strings contained in a file.
# The script should take one argument: the name of the file to read
# The resulting output should be written to the current directory in a  file named not_pii_output.py
# The script should first check if there are no quotes in the file already
# If there are no quotes in the file already, the script should insert quotes around each string
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
    if len(sys.argv) != 2:
        print('Usage: {} <input_file>'.format(sys.argv[0]))
        sys.exit(1)
    with open('not_pii_output.py', 'w') as f:
        f.write(insert_quotes(sys.argv[1]))


if __name__ == '__main__':
    main()
