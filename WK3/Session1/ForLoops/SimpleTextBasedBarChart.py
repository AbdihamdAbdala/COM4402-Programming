numbers_list = []
numbers_count = int(input("Enter how many numbers:"))
bar = ""

for i in range(numbers_count):
    positive_number = int(input("Enter a positive number:"))
    numbers_list.append(positive_number)

for x in numbers_list:
    bar = ""
    for y in range(x):
        bar += "*"
    print(bar)

