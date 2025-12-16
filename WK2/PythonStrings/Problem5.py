# Message Customiser with .replace()
name = input("Enter name:").strip()
course = input("Enter course:").strip()
template = "Hello NAME, welcome to COURSE."

message = template.replace("NAME", name)
message = message.replace("COURSE", course)

print(message)
