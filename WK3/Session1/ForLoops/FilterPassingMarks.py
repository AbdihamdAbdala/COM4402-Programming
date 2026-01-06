pass_count = 0
marks = int(input("Enter how many marks:"))

for i in range(marks):
    mark = int(input("Enter mark:"))
    if mark > 39:
        pass_count += 1
        print(f"Passed: {mark}")

print(f"{pass_count} has passed!")