"""
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

def usermeta_cleaner():
    """Clean up the usermeta table in the database."""
    # Get the name of the csv file to clean up
    csv_file = sys.argv[1]
    fpath = os.path.join(os.getcwd(), csv_file)
    # save the new file in the same directory as the original file, appending '_usermeta_cleaned' to the filename
    new_file = os.path.join(os.path.dirname(fpath), os.path.basename(fpath) + '_usermeta_cleaned.csv')

     # Create a list of PII
    pii = [field for field in csv.DictReader(open(fpath)).fieldnames if field not in [
        "first_name",
        "firstname"
        "nickname"
        "last_name",
        "email",
        "phone",
        "address",
        "city",
        "state",
        "zip",
        "country",
        "comment_author",
        "comment_author_email",
        "ip",
        "twitter",
        "facebook",
        "instagram",
        "linkedin",
        "pinterest",
        "youtube",
        "googleplus",
        "skype",
        "snapchat",
        "reddit",
        "tumblr",
        "github",
        "bitbucket",
        "gitlab",
        "stackoverflow",
        "hackernews",
        "quora",
        "medium",
        "stripe",
        "paypal",
        "venmo",
    ]]

    # Create a list of rows that contain PII
    pii_rows = []

    # Open the csv file
    with open(csv_file, "r") as f:
        # Create a csv reader object
        reader = csv.DictReader(f, delimiter=',')

        # Iterate over the rows in the csv file
        for row in reader:
            # Iterate over the PII list
            for item in pii:
                # If the item is in the row, add the row to the pii_rows list
                if item in row:
                    pii_rows.append(row)

    # Create a list of user IDs
    user_ids = []

    # Open the csv file
    with open(csv_file, "r") as f:
        # Create a csv reader object
        reader = csv.DictReader(f, delimiter=',')

        # Iterate over the rows in the csv file
        for row in reader:
            # If the row contains the user ID, add the user ID to the user_ids list
            if "user_id" in row:
                user_ids.append(row[1])

    # Create a list of rows that contain user IDs
    user_id_rows = []

    # Open the csv file
    with open(csv_file, "r") as f:
        # Create a csv reader object
        reader = csv.DictReader(f, delimiter=',')

        # Iterate over the rows in the csv file
        for row in reader:
            # Iterate over the user_ids list
            for user_id in user_ids:
                # If the user ID is in the row, add the row to the user_id_rows list
                if user_id in row:
                    user_id_rows.append(row)

    
    # On the meta_key column, find the rows that contain PII, remove all that do  not contain PII or empty values

    # Open the csv file
    with open(csv_file, "r", encoding='utf-8') as f:
        # Create a csv reader object
        reader = csv.DictReader(f, delimiter=",")

        with open(os.path.join(fpath, new_file), "w", encoding='utf-8') as f:

            # Create a csv writer object
            writer = csv.DictWriter(f, fieldnames=pii, delimiter=",")

            # Write the header row
            writer.writeheader()

            # Iterate over the rows in the csv file
            for row in reader:
                # Iterate over the pii_rows list
                for pii_row in pii_rows:
                    # If the row contains PII, write the row to the new csv file
                    if row["meta_key"] in pii_row:
                        writer.writerow({k: row[k] for k in pii})

if __name__ == "__main__":
    usermeta_cleaner()