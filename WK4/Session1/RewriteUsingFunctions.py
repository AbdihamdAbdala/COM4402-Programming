def isAdult(age):
    if age >= 18:
        return True
    else:
        return False

def print_message(name, age):
    is_adult = isAdult(age)
    if is_adult == True:
        print(f"Hello {name}, you are an adult.")
    else:
        print(f"Hello {name}, you are under 18.")

def get_user_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    is_adult = isAdult(age)
    return [name, age]

user_details = get_user_details()
print_message(user_details[0], user_details[1])
