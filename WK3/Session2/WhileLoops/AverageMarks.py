total_mark = 0
count = 0
while True:
    print("Type -1 to exit")
    mark = int(input("Enter mark:"))
    if mark <= -1:
        print(f"Marks entered: {total_mark}\nAverage Mark: {total_mark /count}")
        break
    total_mark += mark
    count += 1


