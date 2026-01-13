def classify_mark(mark: int) -> str:
    if not type(mark) is int:
        raise TypeError("mark must be an integer")

    if mark < 0 or mark > 100:
        raise ValueError("mark must be between 0 and 100")

    if mark < 40:
        return "Fail"
    elif mark < 70:
        return "Pass"
    else:
        return "Distinction"


def calculate_summary(marks: list[int]):
    total = 0
    distinction_count = 0
    fail_count = 0
    average = 0
    for i in marks:
        total += i
        mark_classification = classify_mark(i)
        if mark_classification == "Fail":
            fail_count += 1
        elif mark_classification == "Distinction":
            distinction_count += 1
    try:
        average = total / len(marks)
    except ZeroDivisionError:
        print("Cant divide by zero")
    return int(total), float(average), int(fail_count), int(distinction_count)


