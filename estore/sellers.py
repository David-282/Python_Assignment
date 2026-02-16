from estore.user import User


class Seller(User):

    def __init__(self, name, age, phone_number, password, email_address, home_address):
        super().__init__(name, age, phone_number, password, email_address, home_address)
