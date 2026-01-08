def atm_with_limit():
    balance = 100.0
    withdrawn_today = 0.0
    max_withdraw = 250.0

    while True:
        print("\n=== ATM with Daily Limit ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Show daily withdrawal limit")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"Deposited: {amount:.2f}")
            else:
                print("Deposit amount must be positive")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Withdrawal amount must be positive")
            elif amount > balance:
                print("Insufficient balance")
            elif withdrawn_today + amount > max_withdraw:
                print("Daily withdrawal limit exceeded")
            else:
                balance -= amount
                withdrawn_today += amount
                print(f"Withdrawn: {amount:.2f}")

        elif choice == "3":
            print(f"Current balance: {balance:.2f}")

        elif choice == "4":
            print(f"Withdrawn today: {withdrawn_today:.2f}")
            print(f"Daily limit: {max_withdraw:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

atm_with_limit()