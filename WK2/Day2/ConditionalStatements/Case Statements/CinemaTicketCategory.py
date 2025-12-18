age = int(input("Enter age:"))
match age:
    case a if a < 5:
        print("Free entry")
    case a if a > 4 and a < 18:
        print("Child ticket")
    case a if a > 17 and age < 65:
        print("Adult ticket")
    case a if a > 64:
        print("Senior ticket")
