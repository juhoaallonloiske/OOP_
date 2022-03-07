import random

class Dice:
    def __init__(self):
        self.value = 0

    def roll_dice(self):
        while True:
            if random.randint(1, 6) == 1:
                self.value = 1
            elif random.randint(0, 6) == 2:
                self.value = 2
            elif random.randint(0, 6) == 3:
                self.value = 3
            elif random.randint(0, 6) == 4:
                self.value = 4
            elif random.randint(0, 6) == 5:
                self.value = 5
            else:
                self.value = 6
            break

    def get_dice(self):
        return self.value

def main():
    dice_one = Dice()
    dice_two = Dice()

    print("The dices are rolled...")
    dice_one.roll_dice()
    dice_two.roll_dice()

    dice_sum = dice_one.get_dice() + dice_two.get_dice()


    print("Sum of the values is:", dice_sum)

main()