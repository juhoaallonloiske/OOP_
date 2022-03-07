from task9 import Mammal

class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.student_id = ""


    def set_first_name(self):
        self.first_name = input("Enter student's first name: ")

    def set_last_name(self):
        self.first_name = input("Enter student's last name: ")

    def set_student_id(self):
        self.first_name = input("Enter student's ID: ")


    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_player_id(self):
        return self.student_id

    def __str__(self):
        return f'Student({self.first_name}, {self.last_name}, {self.student_id})'


def main():
    student_one = Student()
    student_two = Student()
    student_three = Student()

    panda = Mammal(1, "melanoleuca", "bear", 1, 100)
    grizzly = Mammal(2, "arctos", "bear", 2, 550)
    fox = Mammal(3, "Vulpes", "Red fox", 1, 10)

    student_one.set_first_name()
    student_one.set_last_name()
    student_one.set_student_id()

    student_two.set_first_name()
    student_two.set_last_name()
    student_two.set_student_id()

    student_three.set_first_name()
    student_three.set_last_name()
    student_three.set_student_id()

    dictionary = {
        student_one.get_player_id(): panda.ID,
        student_two.get_player_id(): grizzly.ID,
        student_three.get_player_id(): fox.ID,
    }

    print(f'First student: {student_one.__str__()} \n'
          f'Mammal name: {panda.name} \n'
          f'Mammal species: {panda.species} \n'
          f'Mammal size: {panda.size} \n'
          f'Mammal weight: {panda.weight} \n')

    print(f'Second student: {student_two.__str__()} \n'
          f'Mammal name: {grizzly.name} \n'
          f'Mammal species: {grizzly.species} \n'
          f'Mammal size: {grizzly.size} \n'
          f'Mammal weight: {grizzly.weight} \n')

    print(f'Second student: {student_three.__str__()} \n'
          f'Mammal name: {fox.name} \n'
          f'Mammal species: {fox.species} \n'
          f'Mammal size: {fox.size} \n'
          f'Mammal weight: {fox.weight} \n')


main()
