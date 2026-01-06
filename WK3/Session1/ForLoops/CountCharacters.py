sentence = input("Enter a sentence:")
count = 0
for i in sentence:
    if i != " ":
        count += 1

print(f"There are {count} non-space chars")