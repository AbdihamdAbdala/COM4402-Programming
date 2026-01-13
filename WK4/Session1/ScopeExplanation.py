total = 0

def add_mark(mark, total):
    total = total + mark
    return total

mark1 = int(input("Enter mark 1: "))
total = add_mark(mark1, total)
mark2 = int(input("Enter mark 2: "))
total = add_mark(mark2, total)
print("Total:", total)

# total needs to be assigned to function parameters and added for add_mark when calling it
