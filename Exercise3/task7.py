

'''
PSEUDOCODE:
print "Welcome to Dice Game! Type s to start"

roll dice_one
roll dice_two
roll dice_three
print "Rolling dices"

if dice_one is equal to dice_two or dice_three
    roll dices again

if dice_one value is greater than dice_two or dice_three
    add points for dice_one
if dice_two value is greater than dice_one or dice_three
    add points for dice_two
if dice_three value is greater than dice_two or dice_one
    add points for dice_three
 
    
if dice wins is equal to one
    print "dice_one and dice_two enters the second round"
    roll dice_one
    roll dice_two
    print "Rolling dice"

if dice_one is equal to dice_two
    roll dices again
    
if dice_one value is greater than dice_two
    add points for dice_one
if dice_two value is greater than dice_one 
    add points for dice_two

if dice wins is equal to two
    print "dice_one won the game!"
    

'''
import random

class Dice:
    def __init__(self):
        self.value = 0
        self.in_game = True

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
    player1 = Dice()
    player2 = Dice()
    player3 = Dice()

    while True:
        print("Round 1: \nThe dices are rolled...")
        player1.roll_dice()
        player2.roll_dice()
        player3.roll_dice()

        if player1.get_dice() > player2.get_dice() and player1.get_dice() == player3.get_dice():
            print("Player 1 loses!")
            player1.in_game = False
        if player2.get_dice() > player1.get_dice() and player2.get_dice() == player3.get_dice():
            print("Player 2 loses!")
            player2.in_game = False
        if player3.get_dice() > player1.get_dice() and player3.get_dice() == player2.get_dice():
            print("Player 3 loses!")
            player2.in_game = False

        if player1.get_dice() < player2.get_dice() and player1.get_dice() < player3.get_dice():
            print("Player 1 loses!")
            player1.in_game = False
        if player2.get_dice() < player1.get_dice() and player2.get_dice() < player3.get_dice():
            print("Player 2 loses!")
            player2.in_game = False
        if player3.get_dice() < player1.get_dice() and player3.get_dice() < player2.get_dice():
            print("Player 3 loses!")
            player2.in_game = False

    print("Round 2: \nThe dices are rolled again...")
    player1.roll_dice()
    player2.roll_dice()
    player3.roll_dice()




    print("Sum of the values is:", dice_sum)

main()

