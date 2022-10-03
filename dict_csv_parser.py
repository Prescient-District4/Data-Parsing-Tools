# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:13:26 2022

@author: andile.mbele
"""


from base64 import encode
import csv
import os
import sys


def dict_parser():
    from pathlib import Path
    # open a file from anywhere in the file system by passing the filename as an argument to the parser module e.g python dict_csv_parser.py --filename
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        fpath = Path(filename).parent
        fname = Path(filename).name.rsplit(".", 1)[
            0] + "_new_generated_file.csv"
        with open(filename, 'r') as f:
            csv_reader = csv.DictReader(f, delimiter='\t')

            with open(os.path.join(fpath, fname), 'a', encoding='utf-8') as new_users_table:
                # Return fieldnames that only have personal identifiable information (PII)
                fieldnames = [field for field in csv_reader.fieldnames if field in [
                    'user_id', 'username', 'email', 'secret_key', 'password', 'comment_author', 'comment_author_email', 'comment_author_IP']]


                csv_writer = csv.DictWriter(
                    new_users_table, fieldnames=fieldnames, delimiter="\t"
                )
                csv_writer.writeheader()

                for row in csv_reader:
                    # Exclude any row that is not included in the fieldnames
                    if row['user_id'] or row['username'] or row['email'] or row['secret_key'] or row['password'] or row['comment_author'] or row['comment_author_email'] or row['comment_author_IP']:
                        csv_writer.writerow(row)    


if __name__ == "__main__":
    dict_parser()
