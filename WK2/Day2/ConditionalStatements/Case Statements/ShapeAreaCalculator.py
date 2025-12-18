shape_type = input("Enter shape:")

match shape_type:
    case "circle":
        radius = int(input("Enter radious:"))
        print(radius * 3.14 ** 2)
    case "square":
        side = input("Enter side:")
        print(side ** 2)
    case "triangle":
        base = int(input("Enter base:"))
        height = int(input("Enter height:"))
        print(0.5 * base * height)
    case "rectangle":
        length = int(input("Enter length:"))
        width = int(input("Enter width:"))
        print(length * width)
    case _:
        print("Invalid shape")