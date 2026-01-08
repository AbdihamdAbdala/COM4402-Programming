balance = 0.0

def atm_simple():
 while True:
        print("\n=== Simple ATM ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            deposit()
            pass
        elif choice == "2":
            withdraw()
            pass
        elif choice == "3":
            show_balance()
            pass
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def deposit():
 global balance
 amount = float(input("Enter amount to deposit: "))
 balance += amount
 print(f"You have deposited: ${amount}, you now have balance: ${balance}")
 return balance

def withdraw():
 global balance
 amount = float(input("Enter amount to withdraw: "))
 if amount <= balance:
  balance -= amount
  print(f"You have withdrawn: ${amount}, you now have balance: ${balance}")
 return balance

def show_balance():
 global balance
 return print(f"Current balance: ${round(balance, 2)}")

atm_simple()
