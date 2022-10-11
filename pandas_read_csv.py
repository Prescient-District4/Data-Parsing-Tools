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

# using pandas to read the csv file

import pandas as pd
import os
import sys
# Import not_pii from not_pii_output.py
from not_pii_output import not_pii


def pandas_read_csv():
    """
    Clean up the usermeta table in the database
    """

    # Read the csv file passed as an argument
    df = pd.read_csv(sys.argv[1])

    # Remove all rows that do not have any PII in them and meta_value is not null
    df = df[~df['meta_key'].isin(not_pii) & df['meta_value'].notnull()]

    # make unique list of meta_key as new columns
    new_columns = df['meta_key'].unique()

    # if there's a userid column, sort using that or use user_id column
    if 'userid' in df.columns:
        df = df.sort_values(by=['userid'])
    else:
        df = df.sort_values(by=['user_id'])

    '''
    Print the number of rows that were deleted
    '''
    print(f"Number of rows deleted: {len(df)}")

    '''

    Print all rows of the csv file without the umeta_id column, \
    append the new columns to the csv, sort the rows by user_id which is an integer
    '''
    # if the file has the column umeta_id, drop it.
    if 'umeta_id' in df.columns:
        df.drop('umeta_id', axis=1).append(pd.DataFrame(
            columns=new_columns))
    else:
        df.append(pd.DataFrame(
            columns=new_columns))

    '''
    Populate the new columns with the meta_value of the corresponding meta_key and user_id, \
    rows with NaN leave them blank and print the first all rows of data to the console
    
    '''
    if 'userid' in df.columns:
        df['userid'] = df['userid'].astype(int)
        df.sort_values(by=['userid'], inplace=True)
        data = df.groupby(['userid', 'meta_key'])[
            'meta_value'].first().unstack().fillna('')
        print(data.head())
    elif 'user_id' in df.columns:
        df['user_id'] = df['user_id'].astype(int)
        df.sort_values(by=['user_id'], inplace=True)
        data = df.groupby(['user_id', 'meta_key'])[
            'meta_value'].first().unstack().fillna('')
        print(data.head())

    else:
        print("No userid or user_id column found")

    '''
    Write data to a csv file and save the csv file in the same directory as \
    the original csv file, append the word "usermeta_cleaned" to the file name
    '''
    data.to_csv(os.path.splitext(sys.argv[1])[0] + '_usermeta_cleaned.csv')


if __name__ == "__main__":
    pandas_read_csv()
