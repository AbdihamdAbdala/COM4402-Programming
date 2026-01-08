stars = 1
spaces = 3

for x in range(4):
    print(" " * spaces + (stars * "*"), end = "")
    stars += 2
    spaces -= 1
    print()