from src.bank_app.account import Account


class Bank:

    def __init__(self, name_of_bank):
        self.account_list = []
        self.name_of_bank = name_of_bank
        self.no_of_accounts = 0

    def create_account(self, name, age, phone_number, pin):
        account = Account(name, age, phone_number, pin)
        account.set_acc_number(self.generate_acc_number(phone_number))

        if self.find_by_account_by_number(account.get_acc_number()) is not None:
            raise ValueError("Account already exists")

        self.account_list.append(account)
        self.no_of_accounts += 1

    def find_by_account_by_number(self, acc_number):
        for account in self.account_list:
            if account.get_acc_number() == acc_number:
                return account
        return None

    def withdraw(self, acc_number, amount, pin):
        account = self.account_finder(acc_number)
        account.withdraw(amount, pin)

    def delete_account(self, acc_number):
        for count in range(len(self.account_list)):
            if self.account_list[count].get_acc_number() == acc_number:
                self.account_list.pop(count)
                self.no_of_accounts -= 1
                break

    def get_no_of_number_acc(self):
        return self.no_of_accounts

    def transfer(self, sender_account, sender_pin, receiver_account, amount):
        sending_account = self.account_finder(sender_account)
        receiving_account = self.account_finder(receiver_account)

        sending_account.withdraw(amount, sender_pin)
        receiving_account.deposit(amount)

    def deposit(self, acc_number, amount):
        account = self.account_finder(acc_number)
        account.deposit(amount)

    def check_balance(self, acc_number, pin):
        account = self.account_finder(acc_number)
        return account.check_balance(pin)

    def generate_acc_number(self, phone_number):
        return phone_number[1:]

    def account_finder(self, acc_number):
        account = self.find_by_account_by_number(acc_number)
        if account is None:
            raise ValueError("Account does not exist")
        return account