# Spot the problem with the following code
# Issue 1: Age stored as a string
# Issue 2: AGE variable should be lowercase
Name = input("Enter your name: ")
age = int(input("Enter your age: "))
age_next_year = age + 1
print("hello", Name, "next year you will be", age_next_year)