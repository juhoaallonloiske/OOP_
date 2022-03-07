
class Instrument:
    def __init__(self, name, model_number, country, maker):
        self.name = name
        self.model_number = model_number
        self.country = country
        self.maker = maker


class Guitar(Instrument):
    def __init__(self, name, model_number, country, maker, guitar_type, strings):
        self.name = name
        self.model_number = model_number
        self.country = country
        self.maker = maker
        self.guitar_type = guitar_type
        self.strings = strings

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Model number: {self.model_number} \n' \
               f'Made in: {self.country} \n' \
               f'Made by: {self.maker} \n' \
               f'Guitar type: {self.guitar_type} \n' \
               f'Amount of strings: {self.strings} \n'

class Piano(Instrument):
    def __init__(self, name, model_number, country, maker, keys):
        self.name = name
        self.model_number = model_number
        self.country = country
        self.maker = maker
        self.keys = keys

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Model number: {self.model_number} \n' \
               f'Made in: {self.country} \n' \
               f'Made by: {self.maker} \n' \
               f'Amount of keys: {self.keys} \n'


def main():
    guitar1 = Guitar("Guitar", 10568, "USA", "Gibson", "Single cut", 6)
    piano1 = Piano("Piano", 25023, "Japan", "Yamaha", 76)

    products = {
        "guitar": guitar1.__str__(),
        "piano": piano1.__str__()
    }

    print(products["guitar"])
    print(products["piano"])


main()
