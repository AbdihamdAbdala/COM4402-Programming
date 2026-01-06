def addSum(a, b):
    return a + b

def subtract(a, b):
    return a - b

while True:
    menu = int(input("=====Menu=====\n1. Add\n2. Subtract\n0. Exit\nEnter option:"))
    match menu:
        case 1:
            num1 = int(input("Input Number 1:"))
            num2 = int(input("Input Number 2"))
            print(f"The total is: {addSum(num1, num2)}")
        case 2:
            num1 = int(input("Input Number 1:"))
            num2 = int(input("Input Number 2:"))
            print(f"The total is: {subtract(num1, num2)}")
        case 0:
            print("Exisiting program")
            break
        case _:
            print("Wrong input")