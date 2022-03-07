from task7 import Dice
from task8 import Car
from mammal import Mammal




def main():
    my_dice = Dice()

    the_car = Car()

    panda = Mammal(1, "melanoleuca", "bear", 1, 100)
    grizzly = Mammal(2, "arctos", "bear", 2, 550)
    fox = Mammal(3, "Vulpes", "Red fox", 1, 10)

    print("Rolling the dice...")
    my_dice.roll_dice()
    print("Value of the dice is:", my_dice.get_dice())

    if my_dice.get_dice() == panda.ID:
        print("Value of the dice matches with panda's ID!")
        if panda.size > the_car.get_size_of_trunk():
            print("The panda does not fit inside the trunk!")
        else:
            print("The panda fits inside the trunk!")
        if panda.weight > the_car.get_maximum_load_limit():
            print("The panda exceeds the car's maximum load limit!")
        else:
            print("The panda does not exceed the car's maximum load limit!")

    elif my_dice.get_dice() == grizzly.ID:
        print("Value of the dice matches with grizzly's ID!")
        if grizzly.size > the_car.get_size_of_trunk():
            print("The grizzly does not fit inside the trunk!")
        else:
            print("The grizzly fits inside the trunk!")
        if grizzly.weight > the_car.get_maximum_load_limit():
            print("The grizzly exceeds the car's maximum load limit!")
        else:
            print("The grizzly does not exceed the car's maximum load limit!")

    elif my_dice.get_dice() == fox.ID:
        print("Value of the dice matches with fox's ID!")
        if fox.size > the_car.get_size_of_trunk():
            print("The fox does not fit inside the trunk!")
        else:
            print("The fox fits inside the trunk!")
        if fox.weight > the_car.get_maximum_load_limit():
            print("The fox exceeds the car's maximum load limit!")
        else:
            print("The fox does not exceed the car's maximum load limit!")
    else:
        print("Value of the dice didn't match any mammal's IDs")


main()


