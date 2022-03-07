from task7 import Dice

dice_list = [[], [], []]


def main():
    dice_one = Dice()
    dice_two = Dice()
    dice_three = Dice()

    rounds = 1

    while True:
        if rounds <= 3:
            print(f'Round {rounds}:')
            print("The dices are rolled...")

            dice_one.roll_dice()
            dice_two.roll_dice()
            dice_three.roll_dice()

            dice_list[0].append(dice_one.get_dice())
            dice_list[1].append(dice_two.get_dice())
            dice_list[2].append(dice_three.get_dice())

            print(f'Dice 1 value = {dice_one.get_dice()} \n'
                  f'Dice 2 value = {dice_two.get_dice()} \n'
                  f'Dice 3 value = {dice_three.get_dice()}')
            rounds += 1
        else:
            break



    while True:
        dice_one_sum = sum(dice_list[0])
        dice_two_sum = sum(dice_list[1])
        dice_three_sum = sum(dice_list[2])

        if dice_one_sum < dice_two_sum and dice_one_sum < dice_three_sum:
            print("Dice 1 wins!")
            break
        elif dice_two_sum < dice_one_sum and dice_two_sum < dice_three_sum:
            print("Dice 2 wins!")
            break
        elif dice_three_sum < dice_one_sum and dice_three_sum < dice_two_sum:
            print("Dice 3 wins!")
            break
        else:
            print(f'Dices are tied!')
            print(f'Extra round:')
            print("The dices are rolled...")

            dice_one.roll_dice()
            dice_two.roll_dice()
            dice_three.roll_dice()

            dice_list[0].append(dice_one.get_dice())
            dice_list[1].append(dice_two.get_dice())
            dice_list[2].append(dice_three.get_dice())


main()