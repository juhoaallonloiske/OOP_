class Car:
    def __init__(self):
        self.__make = ""
        self.__model = ""
        self.__mileage = ""
        self.__price = ""
        self.__color = ""
        self.__maximum_load_limit = 0
        self.__size_of_trunk = 0

    def set_make(self):
        self.__make = input("Enter the make: ")

    def set_model(self):
        self.__model = input("Enter the model: ")

    def set_mileage(self):
        self.__mileage = input("Enter the mileage (km): ")

    def set_price(self):
        self.__price = input("Enter the price (€): ")

    def set_color(self):
        self.__color = input("Enter the color: ")

    def set_maximum_load_limit(self):
        self.__maximum_load_limit = int(input("Enter the maximum load limit (kg): "))

    def set_size_of_trunk(self):
        self.__size_of_trunk = int(input("Enter the size of trunk (litres): "))




    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_maximum_load_limit(self):
        return self.__maximum_load_limit

    def get_size_of_trunk(self):
        return self.__size_of_trunk

    def __str__(self):
        return f'Car({self.__make}, {self.__model}, {self.__mileage}, {self.__price}, {self.__color}, {self.__maximum_load_limit}, {self.__size_of_trunk})'

def main():
    my_car = Car()

    my_car.set_make()
    my_car.set_model()
    my_car.set_mileage()
    my_car.set_price()
    my_car.set_color()
    my_car.set_maximum_load_limit()
    my_car.set_size_of_trunk()

    print(my_car.__str__())

main()