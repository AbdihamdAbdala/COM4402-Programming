
def main():
    minutes = int(input("Enter total parking minutes: "))
    parking_time = convert_minutes(minutes)
    print_time(parking_time[0], parking_time[1])

def print_time(hours, remaining):
    if hours > 0 and remaining > 0:
        print(f"{hours} hour(s) and {remaining} minute(s)")
    elif hours > 0:
        print(f"{hours} hour(s)")
    else:
        print(f"{remaining} minute(s)")

def convert_minutes(mins):
    hours = mins // 60
    remaining = mins % 60

    return [hours, remaining]

main()