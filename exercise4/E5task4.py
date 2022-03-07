from task7 import Dice

""" Jokaisella pelaajalla on oma noppa. Vieritä nopat ja tulosta pelaaja ja pelaajan nopan arvo"""


class Player:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.player_id = ""

    def set_first_name(self):
        self.first_name = input("Enter player's first name: ")

    def set_last_name(self):
        self.last_name = input("Enter player's last name: ")

    def set_player_id(self):
        self.player_id = input("Enter player's ID: ")

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_player_id(self):
        return self.player_id

    def __str__(self):
        return f'Player({self.first_name}, {self.last_name}, {self.player_id})'


def main():
    print("Welcome!")

    player_one = Player()
    player_two = Player()
    player_three = Player()

    dice_one = Dice()
    dice_two = Dice()
    dice_three = Dice()

    player_one.set_first_name()
    player_one.set_last_name()
    player_one.set_player_id()

    player_two.set_first_name()
    player_two.set_last_name()
    player_two.set_player_id()

    player_three.set_first_name()
    player_three.set_last_name()
    player_three.set_player_id()

    print("The dices are rolled...")
    dice_one.roll_dice()
    dice_two.roll_dice()
    dice_three.roll_dice()

    playerDic = {
        player_one.player_id: dice_one.get_dice(),
        player_two.player_id: dice_two.get_dice(),
        player_three.player_id: dice_three.get_dice()
    }

    print(player_one.first_name + "'s score: ", playerDic[player_one.player_id], "\n" +
          player_two.first_name + "'s score: ", playerDic[player_two.player_id], "\n" +
          player_three.first_name + "'s score: ", playerDic[player_three.player_id])


main()
