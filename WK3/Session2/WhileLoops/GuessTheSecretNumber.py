secret = 17

while True:
    guess = int(input("Guess the number"))
    if guess != secret:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
    else:
        print("Well done")
        break