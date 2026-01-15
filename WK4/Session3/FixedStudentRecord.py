students = {}

def create_student(id_number, name, year):
    """Create and store a new student record."""
    students[id_number] = {
        "name": name,
        "year": year
    }
    return students[id_number]

def get_name(student):
    """Return the student's name from the record."""
    return student.get("name")

def get_year(student):
    """Return the student's year of study from the record."""
    return student.get("year")


student1 = create_student("1212", "Abdi", 2019)

print(get_name(student1))  # Abdi
print(get_year(student1))  # 2019
