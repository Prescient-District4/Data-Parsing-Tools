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

                    #  exclusion_fieldnames = [field for field in csv_reader.fieldnames if field not in [
                    # 'comment_date', 'comment_date_gmt','comment_content', 'comment_karma', 'comment_approved', 'comment_approved', 'comment_approved', 'comment_agent', 'comment_type', 'user_activation_key', 'user_status', 'display_name', 'user_registered', 'table']]

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

                #  exclusion_fieldnames = [field for field in csv_reader.fieldnames if field not in [
                #     'comment_date', 'comment_date_gmt','comment_content', 'comment_karma', 'comment_approved', 'comment_approved', 'comment_approved', 'comment_agent', 'comment_type', 'user_activation_key', 'user_status', 'display_name', 'user_registered', 'table', 'notes', 'password_reset_expiry', 'authdata', 'signature', 'template', 'ticketnotifications', 'password_reset_key', 'created_at', 'disabled', 'roleid', 'widget_order', 'hidden_widgets', 'supportdepts', 'password_reset_data', 'language', 'uuid', 'loginattempts', 'homewidgets', 'updated_at', 'authmodule', 'banktype', 'datecreated', 'bankcode', 'gatewayid', 'pwresetexpiry', 'companyname', 'securityqid', 'defaultgateway', 'separateinvoices', 'emailoptout', 'disableautocc', 'groupid', 'cardtype', 'cardlastfour', 'cardnum', 'pwresetkey', 'bankname', 'overideduenotices', 'latefeeoveride', 'overrideautoclose', 'taxexempt', 'status', 'billingcid']]
