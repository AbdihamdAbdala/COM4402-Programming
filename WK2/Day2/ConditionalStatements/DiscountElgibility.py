is_student = input("Are you a student?")
age = int(input("Enter your age:"))

if is_student == "yes" or age < 18:
    print("Discount applied")
else:
    print("No discount")
