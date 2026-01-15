def multiplication_table(n):
    list = []
    if n < 0:
        raise ValueError("Num cannot be less than 0")
    if not type(n) is int:
        raise TypeError("Num needs to be an int")
    for i in range(1, n + 1):
        row = []
        for x in range(1, n + 1):
            row.append(i*x)
        list.append(row)

    return list


print(multiplication_table(3))


