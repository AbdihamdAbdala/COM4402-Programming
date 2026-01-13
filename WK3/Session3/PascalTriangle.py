import math
rows = 10
for i in range(rows):
    for j in range(i + 1):
        print(math.comb(i, j), end=" ")
    print()