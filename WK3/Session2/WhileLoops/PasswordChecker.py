correct_password = "python123"

while True:
    password = input("Enter password:")
    if password == correct_password:
        print("Access Granted!")
        break
    else:
        print("Try again!")