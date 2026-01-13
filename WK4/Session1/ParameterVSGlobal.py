rate = 0.2

def calculate_tax(amount, rate):
    return amount * rate

a = float(input("Enter income:"))
t = float(input("Enter tax as decimal:"))
print(f"Tax: {calculate_tax(a, t)}")

# The advantage of version 2 is that it is more dynamic as it allows you to specify the tax rate without reassigning the global variable