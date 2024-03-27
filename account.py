"""
A module for a DSBank acount.
"""

import random
import string

import database as db


class Account:
    """Bank Account model"""

    def __init__(self, full_name, email, phone_number, address, pin):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.pin = pin
        self.balance = 0
        self.account_number = Account.generate_account_number()
        self.transactions = []

    def __str__(self) -> str:
        return f"{self.full_name} -- {self.account_number}"

    def __repr__(self) -> str:
        return f"Account('{self.full_name}', '{self.email}', '{self.phone_number}', '{self.address}', '{self.pin}')"

    @staticmethod
    def get_all_accounts():
        db.get_all_accounts()

    @staticmethod
    def generate_account_number():
        """Generate 10 digits for account number"""
        return "".join(random.choices(string.digits, k=10))

    def obj_to_dict(self):
        obj_dict = {
            "full_name": self.full_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "pin": self.pin,
            "transactions": self.transactions,
            "account_number": self.account_number,
        }
        return obj_dict


def open_account() -> Account:
    # Ask for the user info
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    pin = input("Enter your pin: ")
    confirm_pin = input("Confirm your pin: ")

    # validate user pin
    if pin != confirm_pin:
        raise ValueError("Pin not match.")

    # construct user into dict
    user_data = {
        "full_name": full_name,
        "email": email,
        "phone_number": phone_number,
        "address": address,
        "pin": pin,
    }

    # create an account for user
    new_user = Account(**user_data)  # -->
    # new_user = Account(
    #     full_name=full_name,
    #     email=email,
    #     phone_number=phone_number,
    #     address=address,
    #     pin=pin,
    # )

    # save user into database (ACCOUNTS)
    # db.ACCOUNTS.append(new_user.obj_to_dict())

    db.add_to_db(new_user.obj_to_dict())


# TODO: Future features
# class Tier1Account(Account):
#     pass

# class Tier2Account(Account):
#     pass

# class Tier3Account(Account):
#     pass
