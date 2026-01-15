seats = []

def create_row(names):
    global seats
    seats = names.copy()

def get_student_at(index):
    return seats[index]

def swap_seats(index1, index2):
    seats[index1], seats[index2] = seats[index2], seats[index1]

def remove_student(name):
    seats.remove(name)

create_row(["Lai-Yen", "Cosmin", "Rayyan", "Abdi"])
swap_seats(0, 2)
remove_student("Cosmin")
print(seats)

