
days_late = int(input("Enter days:"))
match days_late:
    case d if d == 0:
        print("No fine")
    case d if d >= 1 and d < 6:
        print("Fine = £1")
    case d if d >= 6 and d < 11:
        print("Fine = £5")
    case _:
        print("Fine = £10 and membership review")