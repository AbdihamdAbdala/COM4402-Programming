# Receipt with Formatting
item_name = input("Input item name:")
price = float(input("Enter price:"))
quantity = int(input("Enter quantity:"))
total = price * quantity
print(f'You bought {quantity} x {item_name} at £{price} each. Total = £{total}')