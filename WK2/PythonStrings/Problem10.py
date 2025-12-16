# Style Comparison Exercise
name = "Sam"
age = 19
course = "COM4402"

# Standard approach for string concatenation in many languages, hard to manage if concat is long but less overhead compared to f string
print("Hello " + name + ", you are " + str(age) + " and enrolled in " + course + ".")
# Easier to use than the first, however, harder to manage especially if concatenation is long.
print("Hello", name + "," + " you are", str(age), "and enrolled in", course + ".")
# Easiest to use, however, possibly more overhead for python
print(f'Hello {name}, you are {age} and enrolled in {course}.')