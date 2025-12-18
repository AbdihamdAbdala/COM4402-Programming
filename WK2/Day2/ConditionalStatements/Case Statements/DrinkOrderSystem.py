drink = input("What is your drink?").lower()
match drink:
    case "coffee":
        price = 2.5
    case "tea":
        price = 1.8
    case _:
        price = 0

print("Order: " + drink, "with price: " + str(price))