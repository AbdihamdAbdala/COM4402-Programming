balance = 0.0

def deposit(b):
    amount = float(input("Amount to deposit: "))
    if amount > 0:
        b += amount
        print(f"Deposited: {amount}")
    else:
        print("Invalid amount.")
    return b

def withdraw(b):
    amount = float(input("Amount to withdraw: "))
    if amount > 0 and amount <= b:
        b -= amount
        print(f"Withdrawn: {amount}")
    else:
        print("Invalid amount or insufficient funds.")
    return b

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            balance = deposit(balance)
            print(f"Current balance: {balance}")
        case 2:
            balance = withdraw(balance)
            print(f"Current balance: {balance}")
        case 0:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice.")
