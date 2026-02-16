from estore.billing_information import BillingInformation
from estore.shopping_cart import ShoppingCart
from estore.user import User


class Customers(User):

    def __init__(self, name, age, phone_number, password, email_address, home_address, billing_information: BillingInformation, shopping_cart : ShoppingCart):
        super().__init__(name, age, phone_number, password, email_address, home_address)
        self.__billing_information =billing_information
        self.__shopping_cart= ShoppingCart()

