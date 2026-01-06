while True:
    positive_num = int(input("Enter a positive integer:"))
    if positive_num <= 0:
        print("Error. Ask again!")
    else:
        print(f"You entered: {positive_num}")
        break