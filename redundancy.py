# del row['username_date']
                    # del row['xfrm_resource_count']
                    # del row['dbtech_shop_immunity']
                    # del row['message_count']
                    # del row['dbtech_credits_lastdaily']
                    # del row['siropu_chat_is_sanctioned']
                    # del row['dbtech_shop_purchases']
                    # del row['snog_flag']
                    # del row['permission_combination_id']
                    # del row['siropu_chat_status']
                    # del row['xfa_rmmp_user_sales']
                    # del row['user_group_id']
                    # del row['vote_score']
                    # del row['security_lock']
                    # del row['bs_telegram_user_id']
                    # del row['dbtech_credits_lastinterest']
                    # del row['avatar_date']
                    # del row['terms_accepted']
                    # del row['trophy_points']
                    # del row['avatar_width']
                    # del row['dbtech_credits_credits']
                    # del row['avatar_height']
                    # del row['table']
                    # del row['siropu_chat_message_count']
                    # del row['dbtech_shop_item_count']
                    # del row['visible']
                    # del row['dbtech_shop_purchase']
                    # del row['conversations_unread']
                    # del row['register_date']
                    # del row['xfa_rmmp_user_cgv']
                    # del row['display_style_group_id']
                    # del row['alerts_unviewed']
                    # del row['CMTV_QT_best_answer_count']
                    # del row['is_staff']
                    # del row['xfa_rmmp_user_purchases']
                    # del row['xfa_rmmp_user_sales_amount']
                    # del row['is_banned']
                    # del row['last_summary_email_date']
                    # del row['siropu_chat_room_join_time']
                    # del row['siropu_chat_settings']
                    # del row['siropu_chat_room_id']
                    # del row['custom_title']
                    # del row['activity_visible']
                    # del row['is_moderator']
                    # del row['siropu_chat_conv_id']
                    # del row['timezone']
                    # del row['username_date_visible']
                    # del row['avatar_highdpi']
                    # del row['privacy_policy_accepted']
                    # del row['is_admin']
                    # del row['last_activity']
                    # del row['warning_points']
                    # del row['reaction_score']
                    # del row['dbtech_credits_lastpaycheck']
                    # del row['siropu_chat_last_activity']
                    # del row['xp_nt_see_newstickers']
                    # del row['siropu_chat_conversations']
                    # del row['question_solution_count']
                    # del row['siropu_chat_rooms']
                    # del row['style_id']
                    # del row['secondary_group_ids']
                    # del row['xfa_rmmp_user_paypal']
                    # del row['dbtech_shop_points']
                    # del row['dbtech_shop_pendingtrades']
                    # del row['alerts_unread']
                    # del row['gravatar']
                    # del row['language_id']
                    # del row['user_state']
                    # del row['dbtech_credits_lasttaxation']

                    # csv_writer.writerow(row)

                    # delete row if it has no personal information  
                    # if not any(row.values()):
                    #     continue
                    # # delete row if it has no email address
                    # if not row['email']:
                    #     continue
                    # # delete row if it has no phone number
                    # if not row['phone_number']:
                    #     continue
                    # # delete row if it has no first name
                    # if not row['first_name']:
                    #     continue
                    # # delete row if it has no last name
                    # if not row['last_name']:
                    #     continue
                    # # delete row if it has no address
                    # if not row['address']:
                    #     continue
                    # # delete row if it has no city
                    # if not row['city']:
                    #     continue
                    # # delete row if it has no state
                    # if not row['state']:
                    #     continue
                    # # delete row if it has no zip code
                    # if not row['zip_code']:
                    #     continue
                    # # delete row if it has no country
                    # if not row['country']:
                    #     continue
                    # # delete row if it has no user id
                    # if not row['user_id']:
                    #     continue
                    # # delete row if it has no password
                    # if not row['password']:
                    #     continue
                    # # delete row if it has no comment author
                    # if not row['comment_author']:
                    #     continue
                    # # delete row if it has no comment author email
                    # if not row['comment_author_email']:
                    #     continue
                    # # delete row if it has no comment author IP
                    # if not row['comment_author_IP']:
                    #     continue
                    # # delete row if it has no comment author IP
                    # if not row['comment_author_IP']:
                    #     continue

                     exclusion_fieldnames = [field for field in csv_reader.fieldnames if field not in [
                    'comment_date', 'comment_date_gmt','comment_content', 'comment_karma', 'comment_approved', 'comment_approved', 'comment_approved', 'comment_agent', 'comment_type', 'user_activation_key', 'user_status', 'display_name', 'user_registered', 'table']]