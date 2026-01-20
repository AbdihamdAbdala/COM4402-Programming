import random # necessary, used for random.shuffle() function

# List of questions and their answers
questionBank = [
    {
        "question": "What is 1+1?",
        "options": ["1", "2", "3"],
        "answer": "2",
        "difficulty": "easy"
    },
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin"],
        "answer": "Paris",
        "difficulty": "easy"
    },
    {
        "question": "Which language is this quiz written in?",
        "options": ["Java", "Python", "C++"],
        "answer": "Python",
        "difficulty": "easy"
    }
]

def start_quiz():
    score = 0
    random.shuffle(questionBank) # randomize the questions

    for i in range(len(questionBank)):
        q = questionBank[i]
        print(f"\nQuestion {i + 1}: {q['question']}")

        for j in range(len(q["options"])):
            print(f"Option ({j + 1}) {q['options'][j]}")

        answer = input("Answer (option number or text): ")

        # try catch block to check if answer is an int and index. this is because the answer can also be the index to the answer in the list
        try:
            index = int(answer) - 1
            user_answer = q["options"][index]
        except ValueError:
            user_answer = answer

        if user_answer.lower() == q["answer"].lower():
            score += 1

    print(f"\nYou have scored {score} out of {len(questionBank)}")


def view_questions():
    print("\n--- Question Bank ---")

    for i in range(len(questionBank)):
        q = questionBank[i]
        print(f"\nQuestion {i + 1}: {q['question']}")
        print("Options:", q["options"])
        print("Difficulty:", q["difficulty"])


def main_menu():
    while True:
        print("\n=== WELCOME TO THE QUIZ MENU ===")
        print("1. Start Quiz")
        print("2. Look at Questions")
        print("3. Exit")

        choice = input("Choose an option: ")

       # check if option is a number, if not throw error
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            continue

        if choice == 1:
            start_quiz()
        elif choice == 2:
            view_questions()
        elif choice == 3:
            print("Exit program")
            break
        else:
            print("Wrong choice")

main_menu()
