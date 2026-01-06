username = "stefan"
password = "knorr"
attempts = 0

while True:
    if attempts > 2:
        print("Account locked!")
        break
    user_input = input("Enter username:")
    password_input = input("Enter password:")

    if user_input == username and password_input == password:
        print("Login succcesful")
        break
    else:
        print("Unsuccessful login")
    attempts += 1
