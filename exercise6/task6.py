from domesticanimal import DomesticAnimal
from wildanimal import WildAnimal

class Participant:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Teacher(Participant):
    def __init__(self, first_name, last_name, age, teacher_id, years_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.teacher_id = teacher_id
        self.years_taught = years_taught

    def __str__(self):
        return f'First name: {self.first_name} \n' \
               f'Last name: {self.last_name} \n' \
               f'Age: {self.age} \n' \
               f'Teacher ID: {self.teacher_id} \n' \
               f'Years taught: {self.years_taught} \n'

class Student(Participant):
    def __init__(self, first_name, last_name, age, student_id, years_studied):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.years_studied = years_studied

    def __str__(self):
        return f'First name: {self.first_name} \n' \
               f'Last name: {self.last_name} \n' \
               f'Age: {self.age} \n' \
               f'Student ID: {self.student_id} \n' \
               f'Years studied: {self.years_studied} \n'

def main():
    teacher = Teacher("John", "Smith", 30, 13469, 10)
    student = Student("Will", "Smithers", 23, 22346, 3)
    domestic_animal1 = DomesticAnimal(6, "Dog", "Goldie", 0.7, 25, "John", "BARK!", "Dog food")
    wild_animal1 = WildAnimal(8, "Bear", "Unknown", 2, 200, "ROAR!", "Fish, grasses, roots, berries", "Brown")
    domestic_animal2 = DomesticAnimal(5, "cat", "Garfield", 0.5, 15, "Jonathan", "meow", "Lasagna")
    wild_animal2 = WildAnimal(9, "Hog", "Unknown", 1, 100, "oink!", "Plants", "Black / Gray")

    pair1 = [teacher.__str__(), domestic_animal1.__str__(), wild_animal1.__str__()]
    pair2 = [student.__str__(), domestic_animal2.__str__(), wild_animal2.__str__()]

    print(pair1)
    print(pair2)


main()

