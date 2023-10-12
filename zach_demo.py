import json

email_with_name_number = {}

# Load data from json files
email_names = json.load(open('email_names[1].json'))
email_numbers = json.load(open('email_numbers[1].json'))

# get unique emails keys
key_email_name = {data["email"]: data for data in email_names}
key_email_number = {data["email"]: data for data in email_numbers}

# add CC number in to found email data with name
for email in key_email_name:
    if email in key_email_number:
        key_email_name[email]["cc_number"] = key_email_number[email]["cc_number"]
        email_with_name_number[email] = key_email_name[email]