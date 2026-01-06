start_number = int(input("Enter start number:"))

while start_number:
    if start_number < 1:
        print("Lift off!")
        start_number -= 1
        break;
    else:
        print("Countdown", start_number)
        start_number -= 1

