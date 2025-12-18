module_mark = int(input("Enter module mark:"))
exam_mark = int(input("Enter exam mark:"))
average = (module_mark + exam_mark) / 2
match (module_mark, exam_mark, average):
    case (m, e) if m < 35 or e < 35:
        print("Automatic fail (component below 35)")
    case (m, e, a) if a >= 40:
        print("Module passed")
    case _:
        print("Module failed")