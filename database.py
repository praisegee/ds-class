import json


def add_to_db(user_dict):
    try:
        # Trying to get the data
        with open("db.json", "r") as f:
            data = json.load(f)

        # add the new user data to account list
        data.append(user_dict)

        # write back to json file
        with open("db.json", "w") as f:
            json.dump(data, f, indent=4)

    except FileNotFoundError:
        with open("db.json", "w") as f:
            json.dump([user_dict], f, indent=4)


def get_all_accounts():
    with open("db.json", "r") as f:
        accounts = json.load(f)

    for account in accounts:
        print(account)


# ACCOUNTS = [
#     {
#         "full_name": "PraiseGod",
#         "email": "me@you.com",
#         "phone_number": "12345678",
#         "address": "New address",
#         "pin": "1234",
#         "account_number": "2738491726",
#         "transactions": [],
#     },
#     {
#         "full_name": "Eminence",
#         "email": "eminence@you.com",
#         "phone_number": "1823738",
#         "address": "New address",
#         "pin": "1234",
#         "account_number": "8273610384",
#         "transactions": [],
#     },
# ]
