# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:13:26 2022

@author: Andile Mbele
"""


from base64 import encode
import csv
import os
import sys

# For any CSV files that are too large to be parsed, we can trick the parser by changing the max size of the file that can be parsed
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def dict_parser():
    from pathlib import Path
    # open a file from anywhere in the file system by passing the filename as an argument to the parser module e.g python dict_csv_parser.py --filename
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        fpath = Path(filename).parent
        # create a new folder named 'cleaned' in the same directory as the file to be parsed and save the parsed file there
        new_dir = os.path.join(fpath, 'cleaned')
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        # create a new file in the 'cleaned' folder and save the parsed file there
        fname = os.path.join(new_dir, 'cleaned_' + os.path.basename(filename))

        with open(filename, 'r', encoding='utf8') as f:
            csv_reader = csv.DictReader(f, delimiter=',')

            with open(os.path.join(fpath, fname), 'w', encoding='utf8') as new_table:
                # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and set those fields as fieldnames
                fieldnames = [field for field in csv_reader.fieldnames if field in [
                    'first_name', 'firstname', 'last_name', 'lastname', 'email', 'password', 'passwordhash', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id', 'user_pass', 'user_login', 'ID', 'user_nicename', 'user_url', 'user_email', 'meta_value', 'username','phonenumber', 'bankacct', 'currency', 'address2', 'address1', 'postcode', 'issuenumber', 'startdate', 'credit', 'email_preferences', 'host', 'hostname', 'ip', 'ipaddress', 'ip_address', 'ipaddr', 'userid', 'nameservers', 'amount', 'ordernum', 'invoiceid', 'paymentmethod', 'domain', 'firstpayment', 'dedicatedip', 'company', 'companyname', 'name', 'nickname', 'confirmed_ip', "lat", "lon", "latitude", "longitude", "Social title", "First name", "Last name", "Email address", 'iso', 'iso3', 'phonecode', 'addr_title',  'phone_num', ' addr_title', 'location', 'flat_no', 'billing_addr', 'billing_address', 'profile', 'email_to', 'email_from', 'email_tobcc', 'email_subject', 'fk_user', 'fk_user_author', 'owner_address', 'birthday', 'birth_day', 'dob', 'zip', 'skype', 'skype_addr', 'skype_address', 'phone', 'phone_mobile', 'gender', 'sex', 'job', 'office_phone', 'user_mobile', 'salary', 'client_ip_address']]
        
                csv_writer = csv.DictWriter(
                    new_table, fieldnames=fieldnames, delimiter=","
                )
                csv_writer.writeheader()

                for row in csv_reader:
                    # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and write those fields to the new file
                    # delete empty rows
                    csv_writer.writerow({k: v for k, v in row.items() if k in fieldnames})
                    # csv_writer.writerow({k: row[k] for k in fieldnames})
                    
                    # Print success message to the console
                print('Successfully parsed file and saved to cleaned folder')
                    # once the file has been parsed, print the path to the new file

                print(f'Parsed file saved to {os.path.join(fpath, fname)}')

if __name__ == "__main__":
    dict_parser()
