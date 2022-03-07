import random

class CellPhone:
    def __init__(self):
        self.manufacturer = ""
        self.model = ""
        self.retail_price = ""
        self.ID = ""

    def set_manufact(self):
        self.manufacturer = input("Enter the manufacturer: ")

    def set_model(self):
        self.model = input("Enter the model number: ")

    def set_retail_price(self):
        self.retail_price = input("Enter the retail price: ")

    def set_ID(self):
            self.ID = int(input("Enter the ID (between 1-6): "))


    def get_manufact(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price

    def get_ID(self):
        return self.ID

    def __str__(self):
        return f'CellPhone({self.manufacturer}, {self.model}, {self.retail_price}, {self.ID})'
