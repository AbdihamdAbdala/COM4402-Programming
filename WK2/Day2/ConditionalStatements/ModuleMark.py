module_mark = int(input("Enter module mark:"))
exam_mark = int(input("Enter exam mark:"))

if module_mark < 35 or exam_mark < 35:
    print("Automatic fail (component below 35)")
elif (module_mark + exam_mark) / 2 >= 40:
    print("Module passed")
else:
    print("Module failed (average below 40)")