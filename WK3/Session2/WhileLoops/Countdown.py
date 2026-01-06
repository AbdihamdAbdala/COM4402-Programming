start_number = int(input("Enter start number:"))

while start_number >= 0:
    if start_number == 0:
        print("Lift off!")
        break
    else:
        print("Countdown", start_number)
    start_number -= 1

