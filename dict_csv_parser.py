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
        with open(filename, 'r', encoding='utf8') as f:
            csv_reader = csv.DictReader(f, delimiter=',')

            with open(os.path.join(fpath, fname), 'w', encoding='utf8') as new_users_table:
                # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and set those fields as fieldnames
                fieldnames = [field for field in csv_reader.fieldnames if field in [
                    'first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id']]
        
                csv_writer = csv.DictWriter(
                    new_users_table, fieldnames=fieldnames, delimiter=","
                )
                csv_writer.writeheader()

                for row in csv_reader:
                    del row['comment_date']
                    del row['comment_date_gmt']
                    del row['comment_content']  
                    del row['comment_karma']    
                    del row['comment_approved'] 
                    del row['comment_agent']    
                    del row['comment_type']
                    del row['comment_parent']
                    del row['user_id']
                    # del row['comment_author_url']
                    del row['comment_ID']
                    del row['comment_post_ID']
                    del row['table']

                    csv_writer.writerow(row)


if __name__ == "__main__":
    dict_parser()
