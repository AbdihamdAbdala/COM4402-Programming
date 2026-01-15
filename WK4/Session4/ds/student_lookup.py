students = {
    "Aisha": 85,
    "Bilal": 72,
    "Chen": 90
}

def find_mark(students, name):
    """
    Look up a student's mark by name.
    students: dict mapping names (str) to marks (int)
    name: str
    Return the mark (int) if the name exists, otherwise return None.
    Raise TypeError if students is not a dict or name is not a str.
    """
    if not type(students) is dict:
        raise TypeError("Not a dict")

    if not type(name) is str:
        raise TypeError("Not a string")

    if name in students:
        return students[name]
    return None