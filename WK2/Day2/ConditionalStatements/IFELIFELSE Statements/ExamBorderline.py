score = int(input("Enter score:"))
if score >= 43:
    print("Clear pass.")
else:
    if score >= 38 and score < 43:
        print("Borderline pass, consider review.")
    else:
        print("Fail")