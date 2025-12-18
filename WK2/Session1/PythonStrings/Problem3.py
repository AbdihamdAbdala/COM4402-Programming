# Tidy Name & Course
full_name = input("What is your full name:")
course_name = input("What is your course name:")

full_name = full_name.strip()
course_name = course_name.strip()

full_name = full_name.title()
course_name = course_name.upper()

print(f'Student: {full_name} ({course_name})')
