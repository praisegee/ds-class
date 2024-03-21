"""
A module for a DSBank acount.
"""


class Account:
    """Bank Account model"""

    def __init__(self, full_name, email, phone_number, address, pin):
        self.full_name = full_name
        self.Phone_number = phone_number
        self.email = email
        self.address = address
        self.pin = pin


def open_account() -> Account:
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    pin = input("Enter your pin: ")
    confirm_pin = input("Confirm your pin: ")

    if pin != confirm_pin:
        raise ValueError("Pin not match.")

    new_user = {
        "full_name": full_name,
        "email": email,
        "phone_number": phone_number,
        "address": address,
        "pin": pin,
    }

    return Account(**new_user)


# TODO: Future features
# class Tier1Account(Account):
#     pass

# class Tier2Account(Account):
#     pass

# class Tier3Account(Account):
#     pass
