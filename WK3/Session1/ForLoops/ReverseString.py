word = input("Enter a word: ")
reverse = ""

for i in range(len(word) - 1, -1, -1):
    reverse += word[i]

print(f"The reverse is: {reverse}")
