"""
@author:  Andile Mbele
program:  usermeta_cleaner.py
Date:     6 October 2022   

Write a script that will clean up the usermeta table in the database. The script should take a single argument, which is the name of the csv file to clean up. The script should remove all rows from the usermeta table that do not have a corresponding user_id in the users table. The script should print out the number of rows that were deleted.

The script should delete all rows that do not have any personal identifiable information (PII) in them. PII is defined as any of the following:
    1. First name   
    2. Last name
    3. Email address    
    4. Phone number
    5. Address
    6. City 
    7. State
    8. Zip code
    9. Country
    10. Comment author
    11. Comment author email
    12. IP
    13. Twitter handle
    14. Facebook handle
    15. Instagram handle
    16. LinkedIn handle
    17. Pinterest handle
    18. YouTube handle
    19. Google+ handle
    20. Skype handle
    21. Snapchat handle
    22. Reddit handle
    23. Tumblr handle
    24. Github handle
    25. Bitbucket handle
    26. Gitlab handle
    27. Stackoverflow handle
    28. Hackernews handle
    29. Quora handle
    30. Medium handle
    31. Stripe handle
    32. Paypal handle   
    33. Venmo handle
"""

import csv  
import os
import sys
from typing import Any

# For any CSV files that are too large to be parsed, we can trick the parser by changing the max
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def usermeta_cleaner() -> Any:
    """Clean up the usermeta table in the database."""
    # Get the name of the csv file to clean up
    csv_file = sys.argv[1]
    fpath = os.path.join(os.getcwd(), csv_file)
    # save the new file in the same directory as the original file, appending '_usermeta_cleaned' before the file extension
    # e.g. if the original file is 'usermeta.csv', the new file will be 'usermeta_usermeta_cleaned.csv'
    # new_file = csv_file.split('.')[0] + '_usermeta_cleaned' + csv_file.split('.')[1] 
    new_file = os.path.join(os.path.dirname(fpath), os.path.basename(fpath) + '_usermeta_cleaned.csv')

     # Create a list of PII
    not_pii =  [
        'gettr',
        '_woocommerce_persistent_cart',
        'wp_woocommerce_persistent_cart',
        'wpseo_keyword_analysis_last_run',
        'wpseo_keyword_analysis-disable',
        'wpseo_linkdex',
        '_yoast_wpseo_profile_updated',
        'syntax_highlighting',
        'dismissed_wp_pointers',
        '_yoast_wpseo_profile_updated',
        'last_update',
        'wpm8_googlesitekit_site_verified_meta',
        'mailchimp_woocommerce_is_subscribed',
        'meta-box-order_post',
        'comment_shortcuts',
        'rich_editing',
        'metaboxhidden_nav-menus',
        '_woocommerce_tracks_anon_id',
        '_yoast_wpseo_profile_updated',
        'wc_last_active',
        'mailchimp_woocommerce_is_subscribed',
        'wpm8_dashboard_quick_press_last_post_id',
        'locale',
        'admin_color',  
        'use_ssl',
        'show_welcome_panel',
        'dismissed_wp_pointers',
        'wp_user-settings',
        'wp_user-settings-time',
        'wp_user_roles',
        'wp_capabilities',
        'wp_user_level',
        'wp_dashboard_quick_press_last_post_id',
        'wp_dashboard_primary',
        'wp_dashboard_secondary',
        'obfx_ignore_visit_dashboard_notice',
        'wpm8_googlesitekit_profile',
        '_woocommerce_persistent_cart_1',
        'community-events-location',
        'closedpostboxes_dashboard',
        'wpm8_googlesitekit_access_token',
        'session_tokens',
        'closedpostboxes_post',
        'jetpack_tracks_anon_id',
        'wpm8_dashboard_quick_press_last_post_id',
        'wpm8_googlesitekit_refresh_token',
        'wpm8_googlesitekit_analytics_adsense_linked',
        'wpm8_googlesitekit_analytics',
        'show_admin_bar_front',
        'meta-box-order_dashboard',
        'wpm8_googlesitekit_additional_auth_scopes',
        'wpm8_googlesitekit_analytics_ownership',
        'wpm8_googlesitekit_transient_timeout_googlesitekit_user_input_settings',
        'wpm8_googlesitekit_auth_scopes',
        'wpm8_user_level',
        'wpm8_capabilities',
        'managenav-menuscolumnshidden',
        'wpm8_yoast_notifications',
        'wpm8_googlesitekit_site_verification_file',
        'wpm8_googlesitekitpersistent_dismissed_tours',
        'metaboxhidden_post',
        'metaboxhidden_dashboard',
        'wpm8_googlesitekitpersistent_initial_version',
        'bwg_photo_gallery',
        'jetpack_tracks_wpcom_id',
        'wpm8_user-settings-time',
        'wpm8_user-settings',
        'wpm8_user-settings',
        'wpm8_googlesitekit_access_token_expires_in',
        'wpm8_googlesitekitpersistent_initial_version',
        'dismissed_update_notice',
        'wpm8_googlesitekit_transient_googlesitekit_user_input_settings',
        'wpm8_googlesitekit_access_token_created_at',
        'wpm8_googlesitekit_user_input_state',

    ]

    # Open the csv file
    with open(csv_file, "r", encoding='utf8') as f:
        # Create a csv reader object
        reader = csv.DictReader(f, delimiter=",")

        # Write to the new file
        with open(os.path.join(fpath, new_file), "w", encoding='utf8', newline="") as new_usermeta:
            fieldnames = reader.fieldnames
            # Create a csv writer object
            writer = csv.DictWriter(new_usermeta, fieldnames=fieldnames, delimiter=",")

            # Write the header row
            writer.writeheader()

            # Loop through the csv file
            for row in reader:
                try:
                    if row['meta_key'] not in not_pii and row['meta_value'] != '':
                        # for any row that remains in the meta_key column, make it a header column in the new file. Link to the user_id in the new file
                        # e.g. if the meta_key is 'first_name', the new file will have a column called 'first_name' and the value will be the value in the meta_value column
                        writer.writerow({k: v for k, v in row.items() if k in fieldnames})
                        # debugging
                        print(row)
                except UnicodeEncodeError:  
                    # if the row contains a non-ascii character, skip it
                    continue
                except KeyError:
                    pass

if __name__ == "__main__":
    usermeta_cleaner()