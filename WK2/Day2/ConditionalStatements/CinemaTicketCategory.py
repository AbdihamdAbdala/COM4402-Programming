age = int(input("Enter age"))
if age < 5:
    print("Free entry")
elif age > 4 and age < 18:
    print("Child ticket")
elif age > 17 and age < 65:
    print("Adult Ticket")
elif age > 64:
    print("Senior ticket")
