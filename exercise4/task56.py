from E5task5 import Student
from task7 import Dice
from task9 import Mammal


def main():
    my_student = Student()
    dice_one = Dice()
    dice_two = Dice()

    panda = Mammal(1, "melanoleuca", "bear", 1, 100)
    grizzly = Mammal(2, "arctos", "bear", 2, 550)
    fox = Mammal(3, "Vulpes", "Red fox", 1, 10)

    my_student.set_first_name()
    my_student.set_last_name()
    my_student.set_student_id()

    print("The dices are rolled...")
    dice_one.roll_dice()
    dice_two.roll_dice()

    dice_sum = dice_one.get_dice() + dice_two.get_dice()

    if dice_sum in range(2, 5):
        print("Student's mammal is:", fox.name)
    elif dice_sum in range(6, 9):
        print("Student's mammal is:", panda.name)
    else:
        print("Student's mammal is:", grizzly.name)


main()
