class Account:
    def __init__(self, name, age, phone_number, pin):
        self.balance = 0.0
        self.pin = None
        self.name = None
        self.phone_number = None
        self.age = None
        self.acc_number = None

        self.set_name(name)
        self.set_age(age)
        self.set_phone_number(phone_number)
        self.set_pin(pin)
        self.set_acc_number(phone_number)

    def deposit(self, amount):
        self.balance += max(amount, 0)

    def check_balance(self, user_pin):
        if self.pin != user_pin:
            raise ValueError("Invalid Pin")
        return self.balance

    def withdraw(self, amount, user_pin):
        self.validate_withdrawal(amount, user_pin)
        self.balance -= amount

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_acc_number(self):
        return self.acc_number

    def get_phone_number(self):
        return self.phone_number

    def set_name(self, name):
        self.is_valid_name(name)
        self.name = name.strip()

    def set_age(self, age):
        self.is_valid_age(age)
        self.age = age

    def set_phone_number(self, phone_number):
        self.is_valid_phone_number(phone_number)
        self.phone_number = phone_number

    def set_pin(self, pin):
        self.is_valid_pin(pin)
        self.pin = pin

    def set_acc_number(self, acc_number):
        self.acc_number = acc_number

    def is_valid_pin(self, pin):
        if pin < 1000 or pin > 9999:
            raise ValueError("Pin must be 4-digits only")

    def is_valid_phone_number(self, phone_number):
        if len(phone_number) != 11:
            raise ValueError("Invalid Phone Number")

    def validate_withdrawal(self, amount, user_pin):
        self.validate_positive_amount(amount)
        self.is_validate_pin(user_pin)
        self.is_sufficient_balance(amount)

    def is_valid_age(self, age):
        if age < 18:
            raise ValueError("Age must be 18 or above")

    def is_valid_name(self, name):
        if name is None or name.strip() == "":
            raise ValueError("Name cannot be empty")

    def validate_positive_amount(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw can't be less than 1")

    def is_validate_pin(self, user_pin):
        if self.pin != user_pin:
            raise ValueError("Invalid Pin")

    def is_sufficient_balance(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")