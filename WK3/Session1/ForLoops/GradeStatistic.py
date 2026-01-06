total_marks = 0
average_mark = 0
distinction_count = 0

students = int(input("Enter number of students:"))

for i in range(students):
    mark = int(input("Enter mark"))
    total_marks += mark
    if mark > 69:
        distinction_count += 1
    average_mark = total_marks / students

print(f"Total marks: {total_marks}\nAverage Mark: {average_mark}\nDisctinctions: {distinction_count}")
