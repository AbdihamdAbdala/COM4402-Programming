balance = 100

while True:
    print(f"Your balance is: £{balance}")
    withdrawal_input = int(input("Enter a withdrawal amount:"))
    if withdrawal_input < 1:
        print("Thank you for using this ATM.")
        break
    if withdrawal_input > balance:
        print("You have insufficient funds.")
    else:
        balance -= withdrawal_input
        print(f"You have withdrawn: £{withdrawal_input}, you now have £{balance}.")
    if balance < 1:
        print("You do not have any more funds.")
        break