gpa = int(input("Enter your grade: "))

if 100 >= gpa >= 90:
    print("Your GPA is: A+")
elif 90 > gpa >= 80:
    print("Your GPA is: A")
elif 80 > gpa >= 70:
    print("Your GPA is: B")
elif 70 > gpa >= 60:
    print("Your GPA is: C")
elif 60 > gpa >= 50:
    print("Your GPA is: D")
elif  gpa < 50:
    print("Your GPA is: F")
else:
    print (" error " )
