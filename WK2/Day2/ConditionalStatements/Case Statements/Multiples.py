num = float(input("Enter number:"))
match num:
    case n if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    case n if n % 3 == 0:
        print("Fizz")
    case n if n % 5 == 0:
        print("Buzz")
    case _:
        print("Not match")