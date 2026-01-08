def marks_classification():
    n = int(input("How many marks will you enter? "))
    total = 0
    fail_count = 0
    pass_count = 0
    distinction_count = 0

    # Loop to read each mark
    for i in range(1, n + 1):
        mark = int(input(f"Enter mark {i}: "))
        total += mark
        if mark > 69:
            distinction_count += 1
        elif mark > 39:
            pass_count += 1
        else:
            fail_count += 1
        pass

    # After the loop
    if n > 0:
        average = total / n
    else:
        average = 0

    # TODO: print total, average, fail_count, distinction_count
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Distinctions: {distinction_count}")


marks_classification()