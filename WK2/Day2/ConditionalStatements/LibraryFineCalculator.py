days_late = int(input("Enter days:"))
if days_late == 0:
    print("No fine")
elif days_late >= 1 and days_late < 6:
    print("Fine = £1")
elif days_late >= 6 and days_late < 11:
    print("Fine = £5")
else:
    print("Fine = £10 and membership review")