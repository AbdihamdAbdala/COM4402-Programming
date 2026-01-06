names = int(input("Enter how many names to enter:"))
stored_names = []
count = 0

for i in range(names):
    name = input("Enter name:")
    stored_names.append(name)

letter = input("Enter letter")

for name in stored_names:
    for char in name:
        if char.lower() == letter.lower():
            count += 1
            print(f"There are {count} instances of the letter {letter} in the stored name {name}")
            break