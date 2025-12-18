questionBank = [
    {"question": "What is 1+1?", "options": [1, 2, 3], "answer": 2, "difficulty": "easy"},
    {"question": "What is 2+2?", "options": [2, 3, 4], "answer": 4, "difficulty": "easy"},
    {"question": "What is 3+3?", "options": [6, 7, 8], "answer": 6, "difficulty": "easy"},
    {"question": "What is (4 * 2) + 4?", "options": [21, 18, 12], "answer": 12, "difficulty": "intermediate"},
]

score = 0

for i, q in enumerate(questionBank):
    print(q["question"])

    for j, opt in enumerate(q["options"], start=1):
        print("Option (" + str(j) + ")", opt)

    answer = input("Answer: ")

    if int(answer) == q["answer"]:
        score += 1

print("You have scored", score, "out of", len(questionBank))