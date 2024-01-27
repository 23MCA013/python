class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")
account_number = int(input("Enter Account Number: "))
name = input("Enter Name: ")
account_type = input("Enter Account Type: ")
balance = float(input("Enter Balance: "))
user_account = BankAccount(account_number, name, account_type, balance)
user_account.display_info()
