'''
PSEUDOCODE:

Initialize class CellPhone
    add attribute Manufacturer
    add attribute Model
    add attribute Retail price

    define method set_manufact
        ask user for manufacturer name and assign it to attribute manufacturer

    define method set_model
        ask user for model name and assign it to attribute model

    define method set_retail_price
        ask user for retail price and assign it to attribute retail_price

    define method get_manufact
        return the value of manufacturer to manufacturer attribute

    define method get_model
        return the value of model to model attribute

    define method get_retail_price
        return the value retail_price to retail_price attribute

    print "Here is the data that you provided:
            Manufacturer: manufacturer attribute
            Model number: model attribute
            Retail price: retail_price attribute"
'''

class CellPhone:
    def __init__(self):
        self.manufacturer = ""
        self.model = ""
        self.retail_price = ""

    def set_manufact(self):
        self.manufacturer = input("Enter the manufacturer: ")

    def set_model(self):
        self.model = input("Enter the model number: ")

    def set_retail_price(self):
        self.retail = input("Enter the retail price: ")

    def get_manufact(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail

def main():
    my_phone = CellPhone()

    my_phone.set_manufact()
    my_phone.set_model()
    my_phone.set_retail_price()

    print("Manufacturer:", my_phone.get_manufact(),
          "\nModel number:", my_phone.get_model(),
          "\nRetail price:", my_phone.get_retail_price())


main()