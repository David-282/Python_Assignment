from estore.product import Product


class Item:

    def __init__(self, quantity: int, product: Product):
        self.__quantity = quantity
        self.__product = product