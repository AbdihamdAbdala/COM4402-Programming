def check_password(input_password):
    password = "python123"
    if input_password == password:
        return True
    else:
        return False

def login():
 input_pass = input("Enter password:")
 correct_pass = check_password(input_pass)
 if correct_pass == True:
     print("Welcome!")
 else:
     print("Access denied!")

def main():
    login()
    login()

main()
