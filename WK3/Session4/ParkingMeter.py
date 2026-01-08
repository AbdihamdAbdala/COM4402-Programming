def parking_meter():
    time_minutes = 0
    max_minutes = 120

    while True:
        print("\n=== Parking Meter ===")
        print("1. Insert £1 (30 minutes)")
        print("2. Insert £2 (60 minutes)")
        print("3. Show time remaining")
        print("0. Finish and print ticket")

        choice = input("Enter choice: ")

        if choice == "1":
            if time_minutes + 30 <= max_minutes:
                time_minutes += 30
                print("30 minutes added.")
            else:
                time_minutes = max_minutes
                print("Maximum parking time reached.")

        elif choice == "2":
            if time_minutes + 60 <= max_minutes:
                time_minutes += 60
                print("60 minutes added.")
            else:
                time_minutes = max_minutes
                print("Maximum parking time reached.")

        elif choice == "3":
            hours = time_minutes // 60
            minutes = time_minutes % 60
            print(f"Time remaining: {hours} hour(s) {minutes} minute(s)")

        elif choice == "0":
            print("Printing ticket...")
            hours = time_minutes // 60
            minutes = time_minutes % 60
            print(f"Final time: {hours} hour(s) {minutes} minute(s)")
            break

        else:
            print("Invalid choice")

parking_meter()