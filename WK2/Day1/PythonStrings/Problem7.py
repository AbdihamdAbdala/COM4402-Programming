# Safe Division with Message
num_1 = float(input("Enter number 1:"))
num_2 = float(input("Enter number 2:"))

if num_2 == 0:
    print("Error: cannot divide by zero")
else:
    print(f'{num_1} divided by {num_2} is {num_1 / num_2}')