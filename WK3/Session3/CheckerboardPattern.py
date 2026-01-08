rows = 8
columns = 8

for row in range(rows):
    for column in range(columns):
        if (row + column) % 2 == 0:
            print("#", end = "")
        else:
            print(".", end = "")
    print()
