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
                    'first_name', 'firstname', 'last_name', 'lastname', 'email', 'password', 'passwordhash', 'phone_number', 'address', 'city', 'state', 'zip_code', 'country', 'comment_author', 'comment_author_email', 'comment_author_url', 'comment_author_IP', 'user_id', 'user_pass', 'user_login', 'ID', 'user_nicename', 'user_url', 'user_email', 'meta_value', 'id', 'username','phonenumber', 'bankacct', 'currency', 'address2', 'address1', 'postcode', 'issuenumber', 'startdate', 'credit', 'email_preferences', 'host', 'ip']]
        
                csv_writer = csv.DictWriter(
                    new_users_table, fieldnames=fieldnames, delimiter=","
                )
                csv_writer.writeheader()

                exclusion_fieldnames = [field for field in csv_reader.fieldnames if field not in [
                    'comment_date', 'comment_date_gmt','comment_content', 'comment_karma', 'comment_approved', 'comment_approved', 'comment_approved', 'comment_agent', 'comment_type', 'user_activation_key', 'user_status', 'display_name', 'user_registered', 'table', 'notes', 'password_reset_expiry', 'authdata', 'signature', 'template', 'ticketnotifications', 'password_reset_key', 'created_at', 'disabled', 'roleid', 'widget_order', 'hidden_widgets', 'supportdepts', 'password_reset_data', 'language', 'uuid', 'loginattempts', 'homewidgets', 'updated_at', 'authmodule', 'banktype', 'datecreated', 'bankcode', 'gatewayid', 'pwresetexpiry', 'companyname', 'securityqid', 'defaultgateway', 'separateinvoices', 'emailoptout', 'disableautocc', 'groupid', 'cardtype', 'cardlastfour', 'cardnum', 'pwresetkey', 'bankname', 'overideduenotices', 'latefeeoveride', 'overrideautoclose', 'taxexempt', 'status', 'billingcid']]

                
                for row in csv_reader:
                    # Loop through the csv_reader object and return only fields that contain contain personal identifiable information (PII) and write those fields to the new file
                    csv_writer.writerow({k: row[k] for k in fieldnames})
    
                    # csv_writer.writerow({k: row[k] for k in exclusion_fieldnames})

                # for row in csv_reader:
                #     if 'umeta_id' in row:
                #         del row['umeta_id']

                #     if 'meta_key' in row:
                #         del row['meta_key']

                #     if 'table' in row:
                #         del row['table']
                    
                #     if 'display_name' in row:
                #         del row['display_name']

                #     if 'user_registered' in row:
                #         del row['user_registered']
                    
                #     if 'user_status' in row:
                #         del row['user_status']

                #     if 'user_activation_key' in row:
                #         del row['user_activation_key']
                    
                #     if 'comment_approved' in row:
                #         del row['comment_approved'] 
                    
                #     if 'comment_type' in row:
                #         del row['comment_type']
                    
                #     if 'comment_agent' in row:
                #         del row['comment_agent']
                    
                #     if 'comment_content' in row:
                #         del row['comment_content']

                #     if 'comment_karma' in row:
                #         del row['comment_karma']
                    
                #     if 'comment_date_gmt' in row:
                #         del row['comment_date_gmt']

                #     if 'comment_date' in row:
                #         del row['comment_date']
                    
                #     if 'notes' in row:
                #         del row['notes']    
                    
                #     if 'password_reset_expiry' in row:  
                #         del row['password_reset_expiry']
                    
                #     if 'authdata' in row:
                #         del row['authdata']

                #     if 'signature' in row:  
                #         del row['signature']

                #     if 'template' in row:
                #         del row['template']

                #     if 'ticketnotifications' in row:
                #         del row['ticketnotifications']

                #     if 'password_reset_key' in row:
                #         del row['password_reset_key']

                #     if 'created_at' in row:
                #         del row['created_at']

                #     if 'disabled' in row:
                #         del row['disabled']

                #     if 'roleid' in row:
                #         del row['roleid']

                #     if 'widget_order' in row:
                #         del row['widget_order']

                #     if 'hidden_widgets' in row:
                #         del row['hidden_widgets']

                #     if 'supportdepts' in row:
                #         del row['supportdepts']

                #     if 'password_reset_data' in row:
                #         del row['password_reset_data']

                #     if 'language' in row:
                #         del row['language']

                #     if 'uuid' in row:
                #         del row['uuid']

                #     if 'loginattempts' in row:
                #         del row['loginattempts']
                    
                #     if 'homewidgets' in row:
                #         del row['homewidgets']

                #     if 'updated_at' in row:
                #         del row['updated_at']

                #     if 'authmodule' in row:
                #         del row['authmodule']
                      
                #     csv_writer.writerow(row)


if __name__ == "__main__":
    dict_parser()
