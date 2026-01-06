last_name = ""

while True:
    menu = int(input("MENU\n1. Enter name\n2. Show last name entered\n0. Exit\nEnter option:"))
    match menu:
        case 1:
            name = input("Enter name:")
            last_name = name
        case 2:
            if last_name == "":
                print("Name is empty.")
                continue
            print(f"Last name was: {last_name}")
        case 0:
            print("Exiting loop...")
            break