from estore.adresses import Addresses
from estore.credit_card_information import CreditCardInformation


class BillingInformation:

    def __init__(self, receiver_name: str, phone_number: str, delivery_address:Addresses, credit_card_information: CreditCardInformation):
        self.__receiver_name = receiver_name
        self.__phone_number = phone_number
        self.__credit_card_information = credit_card_information
        self.__delivery_address = delivery_address
