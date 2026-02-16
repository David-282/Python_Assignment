from estore.product_category import ProductCategory


class Product:

    def __init__(self,product_name: str, product_id: str, price:int, product_description:str, product_category: ProductCategory):
        self.__product_name = product_name
        self.__product_id = product_id
        self.__price = price
        self.__product_description = product_description
        self.__product_category = product_category
