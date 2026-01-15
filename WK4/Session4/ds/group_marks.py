def group_marks(marks):
    """Group marks into 'Fail', 'Pass', and 'Distinction
    marks: list of integers (0..100)
    Returns a dict:
    {"Fail": [...],
    "Pass": [...],
    "Distinction": [...]}
    Raise TypeError if marks is not a list or if any element is not int.
    Raise ValueError if any mark is outside 0..100.
    """
    group_marking = {}
    group_marking["Fail"] = []
    group_marking["Pass"] = []
    group_marking["Distinction"] = []

    if not type(marks) is list:
        raise TypeError("Marks is not a list")

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be in range 0-100")
        if mark < 40:
            group_marking["Fail"].append(mark)
        elif mark > 39 and mark < 70:
            group_marking["Pass"].append(mark)
        elif mark > 69:
            group_marking["Distinction"].append(mark)

    return group_marking

print(group_marks([20, 30, 40, 50, 60, 70, 90, 21, 47]))