pin = int(input("Enter pin:"))
if pin == 1234:
    security_question = input("What is your favourite colour?").lower()
    if security_question == "blue":
        print("Access granted")
    else:
        print("Security answer incorrect")
else:
    print("Wrong PIN")