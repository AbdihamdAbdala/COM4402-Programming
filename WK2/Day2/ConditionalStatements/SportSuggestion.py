weather = input("Enter weather:")
mood = input("Enter mood:")
if weather == "sunny" and mood == "active":
    print("Go for a run")
elif weather == "sunny" and mood == "tired":
    print("Relax in the park")
elif weather == "rainy":
    print("Indoor workout")
elif weather == "cold":
    print("Go to the gym")
else:
    print("No suggestion available")