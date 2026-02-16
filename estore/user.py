from estore.adresses import Addresses


class User:

    def __init__(self, name:str ,age: int ,phone_number: str ,password:str ,email_address: str ,home_address: Addresses):
        self.__name = name
        self.__age = age
        self.__phone_number = phone_number
        self.__password = password
        self.__email_address = email_address
        self.__home_address = home_address



