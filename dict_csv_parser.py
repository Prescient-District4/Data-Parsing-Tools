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
            csv_reader = csv.DictReader(f, delimiter=',')
            # for line in csv_reader:
            #     print(line['user_id','username','email', 'secret_key'])

            with open(os.path.join(fpath, fname), 'a', encoding='utf-8') as new_users_table:
                fieldnames = [
                    'user_id', 'username', 'email', 'secret_key'
                ]

                csv_writer = csv.DictWriter(
                    new_users_table, fieldnames=fieldnames, delimiter="\t"
                )
                csv_writer.writeheader()

                for row in csv_reader:
                    del row['username_date']
                    del row['xfrm_resource_count']
                    del row['dbtech_shop_immunity']
                    del row['message_count']
                    del row['dbtech_credits_lastdaily']
                    del row['siropu_chat_is_sanctioned']
                    del row['dbtech_shop_purchases']
                    del row['snog_flag']
                    del row['permission_combination_id']
                    del row['siropu_chat_status']
                    del row['xfa_rmmp_user_sales']
                    del row['user_group_id']
                    del row['vote_score']
                    del row['security_lock']
                    del row['bs_telegram_user_id']
                    del row['dbtech_credits_lastinterest']
                    del row['avatar_date']
                    del row['terms_accepted']
                    del row['trophy_points']
                    del row['avatar_width']
                    del row['dbtech_credits_credits']
                    del row['avatar_height']
                    del row['table']
                    del row['siropu_chat_message_count']
                    del row['dbtech_shop_item_count']
                    del row['visible']
                    del row['dbtech_shop_purchase']
                    del row['conversations_unread']
                    del row['register_date']
                    del row['xfa_rmmp_user_cgv']
                    del row['display_style_group_id']
                    del row['alerts_unviewed']
                    del row['CMTV_QT_best_answer_count']
                    del row['is_staff']
                    del row['xfa_rmmp_user_purchases']
                    del row['xfa_rmmp_user_sales_amount']
                    del row['is_banned']
                    del row['last_summary_email_date']
                    del row['siropu_chat_room_join_time']
                    del row['siropu_chat_settings']
                    del row['siropu_chat_room_id']
                    del row['custom_title']
                    del row['activity_visible']
                    del row['is_moderator']
                    del row['siropu_chat_conv_id']
                    del row['timezone']
                    del row['username_date_visible']
                    del row['avatar_highdpi']
                    del row['privacy_policy_accepted']
                    del row['is_admin']
                    del row['last_activity']
                    del row['warning_points']
                    del row['reaction_score']
                    del row['dbtech_credits_lastpaycheck']
                    del row['siropu_chat_last_activity']
                    del row['xp_nt_see_newstickers']
                    del row['siropu_chat_conversations']
                    del row['question_solution_count']
                    del row['siropu_chat_rooms']
                    del row['style_id']
                    del row['secondary_group_ids']
                    del row['xfa_rmmp_user_paypal']
                    del row['dbtech_shop_points']
                    del row['dbtech_shop_pendingtrades']
                    del row['alerts_unread']
                    del row['gravatar']
                    del row['language_id']
                    del row['user_state']
                    del row['dbtech_credits_lasttaxation']

                    csv_writer.writerow(row)


if __name__ == "__main__":
    dict_parser()
