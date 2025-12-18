grade_letter = input("What is your grade?").upper()
match grade_letter:
    case "A": print("80-100")
    case "B": print("70-79")
    case "C": print("60-69")
    case "D": print("50-59")
    case "E": print("40-49")
    case _: print("Invalid grade")