def add_time(current_minutes: int, minutes_to_add: int, max_minutes: int) -> int:
    if current_minutes <= 0:
        raise ValueError("Current minutes cannot be 0 or below")
    if minutes_to_add > 0 and minutes_to_add < 61:
        raise ValueError("Minutes need to be in range 0-60")
    if max_minutes > 120:
        raise ValueError("Parking time cannot be more than 120")
    if minutes_to_add <= 0:
        raise ValueError("Minutes need to be greater than 0")
    new_total = current_minutes + minutes_to_add
    if new_total > max_minutes:
        return max_minutes
    else:
        return new_total


def convert_minutes(time_minutes: int) -> tuple[int, int]:
    if time_minutes <= 0:
        raise ValueError("Time minutes need to be above 0")
    hours = time_minutes // 60
    remaining_minutes = time_minutes % 60
    return int(hours), int(remaining_minutes)

def format_time(hours: int, minutes: int):
    hours_string = ""
    minutes_string = ""
    if hours < 0:
        raise ValueError("Hours cannot be less than 0")
    if minutes <= 0 or minutes >= 60:
        raise ValueError("Minutes cannot be above 60 or less than 0")
    if hours:
        hours_string = f"{hours} hour(s)"
    if minutes:
        minutes_string = f"{minutes} minute(s)"
    return f"{hours_string} {minutes_string}".lstrip()

hours, mins = convert_minutes(90)
print(format_time(hours, mins))
