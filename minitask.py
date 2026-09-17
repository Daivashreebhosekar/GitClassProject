student_info = input("Enter you name : ")
student_age = int(input("Enter your age: "))
if student_age >0 :
    if student_age > 18  and student_age < 50:
        print("You can enter class ")

    elif student_age < 18:
        print("You cannot enter class ")

    else:
        print("Invalid age")
else:
    print("How can age be negative?")