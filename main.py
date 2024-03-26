"""
A Python Capstone Project for Data Science class.
    Title: DSBank
"""

from account import Account, open_account

OPTIONS = {
    "1": open_account,
    "2": ...,
    "3": ...,
    "4": ...,
    "5": ...,
}


def validate_option(option):
    if option not in ["1", "2", "3", "4", "5"]:
        return False
    return True


def welcome():
    print("Welcome to DSBank: We valued your patronage.")


def get_option():
    option_text = """
    What do you wanna to today? 
    Options:
        1. Open an account with us.
        2. Login to your account if you've already have an account.
        3. Deposit.
        4. Withdraw.
        5. Make Transfer.
        
    Enter any of the options from 1 to 5.
    ==========> """
    return input(option_text)


def home():
    """Welcome the user and ask the user what to do."""
    welcome()


def app():
    welcome()
    option = get_option()
    if not validate_option(option):
        print("Option not valid.")
    else:
        OPTIONS[option]()

    Account.get_all_accounts()


if __name__ == "__main__":
    app()
