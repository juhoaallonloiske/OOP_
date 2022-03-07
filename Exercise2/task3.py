

points = int(input(("Enter amount of points: ")))

if points > 0 and points < 60:
    print("Your grade is 0")
elif points >= 60 and points < 72:
    print("Your grade is 1")
elif points >= 72 and points < 84:
    print("Your grade is 2")
elif points >= 84 and points < 96:
    print("Your grade is 3")
elif points >= 96 and points < 108:
    print("Your grade is 4")
elif points >= 108:
    print("Your grade is 5")
else:
    print('Invalid input')

