from estore.card_type import CardType


class CreditCardInformation:

    def __init__(self,card_cvv: str,card_name: str, credit_card_number: str, card_expiry_date: str, card_type: CardType):
        self.__card_cvv = card_cvv
        self.__card_name = card_name
        self.__credit_card_number = credit_card_number
        self.__card_expiry_date = card_expiry_date
        self.__card_type = card_type