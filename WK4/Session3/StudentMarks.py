# I used a dictionary to quickly search up for information (performance reasons)

student_marks = {}

def add_mark(marks, name, mark):
    marks[name] = mark
    return marks
def get_mark(marks, name):
    if name in marks:
        return marks[name]
    else:
        return None
def update_mark(marks, name, new_mark):
    if name in marks:
        marks[name] = new_mark
        return True
    else:
        return False
def delete_mark(marks, name):
    if name in marks:
        del marks[name]
        return True
    else:
        return False
