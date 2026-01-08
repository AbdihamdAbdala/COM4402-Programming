def login_then_menu():
    correct_user = "admin"
    correct_pass = "python123"
    attempts = 0
    max_attempts = 3

    # Login phase
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")
        if username == correct_user and password == correct_pass:
            print("Login successful")
            break
        else:
            print("Incorrect username or password")
            attempts += 1

        if attempts == max_attempts:
            print("Account locked")
            return  # stop the function here

    # Main menu phase
    while True:
        print("\n=== Main Menu ===")
        print("1. Greet")
        print("2. Show username")
        print("0. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            print_greeting("Hello. Welcome to the Home Menu!")
            pass
        elif choice == "2":
            print_greeting(f"Logged in user: {username}")
            pass
        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("Invalid choice")

def print_greeting(msg):
    print(msg)

login_then_menu()