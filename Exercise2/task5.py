import statistics

student_names = []
student_grades = []


while True:
    answer = input(
        "Would you like to: \n 1. Add student and grade \n 2. Count the average of grades \n 3. Quit \n (1/2/3): ")

    if answer == "1":
        student_names.append(input("Enter student's name: "))
        student_grades.append(int(input("Enter student's grade (0-5): ")))
        continue
    elif answer == "2":
        average = statistics.mean(student_grades)
        print("Average of grades: ", average)
        continue
    elif answer == "3":
        break
