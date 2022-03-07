from card import Deck


def main():
    my_deck = Deck()
    my_deck.shuffle_deck()

    while True:
        print("Let's draw 3 cards")
        print("First draw:")
        card1 = my_deck.draw_card()
        card1.show_card()
        print("Second draw:")
        card2 = my_deck.draw_card()
        card2.show_card()
        print("Third draw:")
        card3 = my_deck.draw_card()
        card3.show_card()

        if card1.value > card2.value and card1.value > card3.value:
            print("The first draw wins!")
            break
        elif card2.value > card1.value and card2.value > card3.value:
            print("The second draw wins!")
            break
        elif card3.value > card1.value and card3.value > card2.value:
            print("The third draw wins!")
            break
        else:
            print("Draw! New cards are drawn.")
            continue


main()
