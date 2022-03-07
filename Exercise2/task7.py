import random


# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):

        if random.randint(0, 4) == 0:
            self.sideup = 'landed with heads side up'
        elif random.randint(0, 4) == 1:
            self.sideup = 'landed with tails side up'
        elif random.randint(0, 4) == 2:
            self.sideup = 'lands on the table upright'
        elif random.randint(0, 4) == 3:
            self.sideup = 'defies gravity and gets lost on a wormhole in space'
        else:
            self.sideup = 'drops on the ground and disappears on a rabbit hole'

    def get_sideup(self):
        return self.sideup


# Main function definition

def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("The coin", my_coin.get_sideup())


# Calling the main function
main()
