colour = input("Enter colour:").lower()
match colour:
    case "red":
        print("Stop")
    case "amber":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Colour")