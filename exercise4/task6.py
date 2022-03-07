from task4class import CellPhone
from task7 import Dice

def main():
    phone_one = CellPhone()
    phone_two = CellPhone()
    phone_three = CellPhone()
    phone_four = CellPhone()
    phone_five = CellPhone()
    phone_six = CellPhone()

    phone_one.set_manufact()
    phone_one.set_model()
    phone_one.set_retail_price()
    phone_one.set_ID()

    phone_two.set_manufact()
    phone_two.set_model()
    phone_two.set_retail_price()
    phone_two.set_ID()

    phone_three.set_manufact()
    phone_three.set_model()
    phone_three.set_retail_price()
    phone_three.set_ID()

    phone_four.set_manufact()
    phone_four.set_model()
    phone_four.set_retail_price()
    phone_four.set_ID()

    phone_five.set_manufact()
    phone_five.set_model()
    phone_five.set_retail_price()
    phone_five.set_ID()

    phone_six.set_manufact()
    phone_six.set_model()
    phone_six.set_retail_price()
    phone_six.set_ID()

    my_dice = Dice()

    print("Rolling the dice...")
    my_dice.roll_dice()

    if my_dice.get_dice() == phone_one.ID:
        print(phone_one.__str__())
    elif my_dice.get_dice() == phone_two.ID:
        print(phone_two.__str__())
    elif my_dice.get_dice() == phone_three.ID:
        print(phone_three.__str__())
    elif my_dice.get_dice() == phone_four.ID:
        print(phone_four.__str__())
    elif my_dice.get_dice() == phone_five.ID:
        print(phone_five.__str__())
    elif my_dice.get_dice() == phone_six.ID:
        print(phone_six.__str__())


main()