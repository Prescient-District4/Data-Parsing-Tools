# Write a script that removes single quotes from strings contained in a python file.
# the script should take one argument: the name of the file to read
# the resulting output should modify the original file
# the script should create a set variable named not_pii and store all the contents in the file in the set

# Save the file as a python module with all the contents stored in a set named not_pii

import sys
import re


def remove_single_quotes(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        text = re.sub(r"'", r'', text)
        return text


def main():
    if len(sys.argv) != 2:
        print('Usage: {} <input_file>'.format(sys.argv[0]))
        sys.exit(1)
    with open(sys.argv[1], 'a') as f:
        f.write(remove_single_quotes(sys.argv[1]))


if __name__ == '__main__':
    main()
