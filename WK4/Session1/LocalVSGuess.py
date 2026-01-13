count = 0

def add_one():
    global count
    count = count + 1
    print("Inside:", count)

add_one()
print("Outside:", count)
