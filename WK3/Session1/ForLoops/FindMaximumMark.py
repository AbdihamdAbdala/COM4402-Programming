highest_mark = 0
marks = int(input("How many marks to enter"))

for i in range(marks):
    num = int(input("Enter marks"))
    if num > highest_mark:
        highest_mark = num

print(f"Highest mark is: {highest_mark}")


