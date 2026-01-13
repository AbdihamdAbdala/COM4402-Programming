def apply_discount(price):
    if price > 100:
        discount = 10
    else:
        discount = 0
    return price - discount

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)
