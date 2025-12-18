# Activity 6: Product Cost
product_name = input("Enter product name:")
price = float(input("Enter price:"))
quantity = int(input("Enter quantity:"))
total_cost = price * quantity
print("You bought " + str(quantity) + " of " + product_name)
print("Total cost is " + str(total_cost))
