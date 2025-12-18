time_of_day = input("Enter time of day:").lower()
is_hungry = input("Are you hungry?").lower()
if is_hungry == "no":
    print("Have some water and rest")
elif is_hungry == "yes":
    if time_of_day == "morning":
        print("Have breakfast")
    elif time_of_day == "afternoon":
        print("Have lunch")
    elif time_of_day == "evening":
        print("Have dinner")
    else:
        print("Snack time")
