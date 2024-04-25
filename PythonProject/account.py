"""
A module for a DSBank acount.
"""

import random
import string

import database as db


class Account:
    """Bank Account model"""

    def __init__(self, full_name: str, email, phone_number, address, pin):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.pin = pin
        self.balance = 0.00
        self.account_number = Account.generate_account_number()
        self.transactions = []

    def __str__(self) -> str:
        return f"{self.full_name} -- {self.account_number}"

    def __repr__(self) -> str:
        return f"Account('{self.full_name}', '{self.email}', '{self.phone_number}', '{self.address}', '{self.pin}')"

    @staticmethod
    def get_all_accounts():
        return db.get_all_accounts()

    @staticmethod
    def generate_account_number():
        """Generate 10 digits for account number"""
        return "".join(random.choices(string.digits, k=10))

    def _format_user_info(account):
        message = f"""
            {account['full_name'].title()} -- {account['account_number']}
            Balance: {account['balance']}
        """
        print(message)

    def deposit(self, amount):
        amount = float(amount)

        if amount < 100:
            print("You must deposit an amount up to or greater than 100")
            return

        self.balance += amount

    @classmethod
    def open_account(cls):

        # Ask for the user info
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ").lower().strip()
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

        new_user = cls(**user_data)
        db.add_to_db(new_user.obj_to_dict())

    def login(self):
        # ask for user email and pin
        email = input("Email: ").lower().strip()
        pin = input("PIN: ")

        if self.email == email and self.pin == pin:
            print("Login successful.")
            self._format_user_info(self.obj_to_dict())
        else:
            print("Incorrect email or pin.")

    def obj_to_dict(self):
        obj_dict = {
            "full_name": self.full_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions,
            "account_number": self.account_number,
        }
        return obj_dict


# TODO: Future features
# class Tier1Account(Account):
#     pass

# class Tier2Account(Account):
#     pass

# class Tier3Account(Account):
#     pass
