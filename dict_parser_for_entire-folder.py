# -*- coding: utf-8 -*-
"""
Created on Mon Oct 3 23:56:26 2022

@author: andile.mbele
"""


from base64 import encode
import csv
import os
import sys

def dict_parser():
    from pathlib import Path
    if len(sys.argv) > 1:
        # because the csv files are so many in the folder, we need to loop through the folder and parse each file
        for filename in os.listdir(sys.argv[1]):
            if filename.endswith(".csv"):
                fpath = Path(filename).parent
                # create a new folder named 'cleaned' in the same directory as the file to be parsed and save the parsed file there
                new_dir = os.path.join(fpath, 'cleaned')
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                # create a new file in the 'cleaned' folder and save the parsed file there
                fname = os.path.join(new_dir, 'cleaned_' + os.path.basename(filename))

                # fname = Path(filename).name.rsplit(".", 1)[
                #     0] + "_new_generated_file.csv"
                with open(filename, 'r', encoding='utf8') as f:
                    csv_reader = csv.DictReader(f, delimiter=',')

                    with open(os.path.join(fpath, fname), 'w', encoding='utf8') as new_users_table:
                        # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and set those fields as fieldnames
                        fieldnames = [field for field in csv_reader.fieldnames if field in [
                            'first_name', 'firstname', 'last_name', 'lastname', 'email', 'password', 'passwordhash', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id', 'user_pass', 'user_login', 'ID', 'user_nicename', 'user_url', 'user_email', 'meta_value', 'id', 'username','phonenumber', 'bankacct', 'currency', 'address2', 'address1', 'postcode', 'issuenumber', 'startdate', 'credit', 'email_preferences', 'host', 'hostname', 'ip', 'ipaddress', 'ip_address', 'ipaddr', 'userid', 'nameservers', 'amount', 'ordernum', 'invoiceid', 'paymentmethod', 'domain', 'firstpayment', 'dedicatedip', 'company', 'companyname', 'name', 'nickname', 'confirmed_ip']]
                        
                        csv_writer = csv.DictWriter(
                            new_users_table, fieldnames=fieldnames, delimiter=","
                        )
                        csv_writer.writeheader()

                        exclusion_fieldnames = [field for field in csv_reader.fieldnames if field not in [
                            'first_name', 'firstname', 'last_name', 'lastname', 'email', 'password', 'passwordhash', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id', 'user_pass', 'user_login', 'ID', 'user_nicename', 'user_url', 'user_email', 'meta_value', 'id', 'username','phonenumber', 'bankacct', 'currency', 'address2', 'address1', 'postcode', 'issuenumber', 'startdate', 'credit', 'email_preferences', 'host', 'hostname', 'ip', 'ipaddress', 'ip_address', 'ipaddr', 'userid', 'nameservers', 'amount', 'ordernum', 'invoiceid', 'paymentmethod', 'domain', 'firstpayment', 'dedicatedip', 'company', 'companyname', 'name', 'nickname', 'confirmed_ip']]
                        
                        for row in csv_reader:
                            # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and set those fields as fieldnames
                            row = {field: row[field] for field in row if field in [
                                'first_name', 'firstname', 'last_name', 'lastname', 'email', 'password', 'passwordhash', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id', 'user_pass', 'user_login', 'ID', 'user_nicename', 'user_url', 'user_email', 'meta_value', 'id', 'username','phonenumber', 'bankacct', 'currency', 'address2', 'address1', 'postcode', 'issuenumber', 'startdate', 'credit', 'email_preferences', 'host', 'hostname', 'ip', 'ipaddress', 'ip_address', 'ipaddr', 'userid', 'nameservers', 'amount', 'ordernum', 'invoiceid', 'paymentmethod', 'domain', 'firstpayment', 'dedicatedip', 'company', 'companyname', 'name', 'nickname', 'confirmed_ip']}
                            csv_writer.writerow(row)
    else:
        print("Please provide the path to the folder containing the csv files to be parsed")

if __name__ == "__main__":
    dict_parser()
