import random

# analytical statistics
question_db_stats = {
    "highest_score": 0,
    "history_scores": [],
    "average_score": 0,
}

# List of questions and their answers
question_db_main = [
    # EASY (5)
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "2",
        "difficulty": "easy",
        "subject": "maths"
    },
    {
        "question": "What planet do we live on?",
        "options": ["Mars", "Venus", "Earth", "Jupiter"],
        "answer": "3",
        "difficulty": "easy",
        "subject": "science"
    },
    {
        "question": "What is 10 × 1?",
        "options": ["1", "5", "10", "20"],
        "answer": "3",
        "difficulty": "easy",
        "subject": "maths"
    },
    {
        "question": "What gas do humans breathe in to survive?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"],
        "answer": "2",
        "difficulty": "easy",
        "subject": "science"
    },
    {
        "question": "How many sides does a triangle have?",
        "options": ["2", "3", "4", "5"],
        "answer": "2",
        "difficulty": "easy",
        "subject": "maths"
    },

    # MEDIUM (5)
    {
        "question": "What is 12 ÷ 3?",
        "options": ["2", "3", "4", "6"],
        "answer": "3",
        "difficulty": "medium",
        "subject": "maths"
    },
    {
        "question": "What part of the plant conducts photosynthesis?",
        "options": ["Roots", "Stem", "Leaves", "Flower"],
        "answer": "3",
        "difficulty": "medium",
        "subject": "science"
    },
    {
        "question": "What is the square root of 81?",
        "options": ["7", "8", "9", "10"],
        "answer": "3",
        "difficulty": "medium",
        "subject": "maths"
    },
    {
        "question": "Which force pulls objects toward Earth?",
        "options": ["Magnetism", "Friction", "Gravity", "Electricity"],
        "answer": "3",
        "difficulty": "medium",
        "subject": "science"
    },
    {
        "question": "What is 7 × 6?",
        "options": ["36", "40", "42", "48"],
        "answer": "3",
        "difficulty": "medium",
        "subject": "maths"
    },

    # HARD (5)
    {
        "question": "What is the value of π (pi) rounded to two decimal places?",
        "options": ["3.12", "3.14", "3.16", "3.18"],
        "answer": "2",
        "difficulty": "hard",
        "subject": "maths"
    },
    {
        "question": "What is the chemical symbol for Sodium?",
        "options": ["So", "Sd", "Na", "S"],
        "answer": "3",
        "difficulty": "hard",
        "subject": "science"
    },
    {
        "question": "What is 15% of 200?",
        "options": ["15", "20", "25", "30"],
        "answer": "4",
        "difficulty": "hard",
        "subject": "maths"
    },
    {
        "question": "Which particle has a negative electric charge?",
        "options": ["Proton", "Neutron", "Electron", "Ion"],
        "answer": "3",
        "difficulty": "hard",
        "subject": "science"
    },
    {
        "question": "Solve: (8 × 5) − (12 ÷ 3)",
        "options": ["34", "36", "38", "40"],
        "answer": "2",
        "difficulty": "hard",
        "subject": "maths"
    }
]

def start_quiz(subject, difficulty):
    score = 0
    incorrect_answers = []
    #question_bank = []
    question_bank = [q for q in question_db_main if q["subject"] == subject]
    question_bank = [q for q in question_bank if q["difficulty"] == difficulty]

    random.shuffle(question_bank) # randomize the questions

    for i in range(len(question_bank)):
        q = question_bank[i]
        print(f"\nQuestion {i + 1}: {q["question"]}")

        for j in range(len(q["options"])):
            print(f"Option ({j + 1}) {q["options"][j]}")

        answer = input("Enter index of answer: ")

        try:
            index = int(answer) - 1
            user_answer = q["options"][index]
        except ValueError:
            print("Invalid choice")
            continue
        except IndexError:
            print("Invalid choice")
            continue

        correct_answer = q["options"][int(q["answer"]) - 1]

        if user_answer.lower() == correct_answer.lower():
            score += 1
        else:
            incorrect_answers.append(f"Question: {q["question"]}\nYour Incorrect Answer: {user_answer}\nCorrect Answer: {correct_answer}")

    calculated_score = score // len(question_bank)
    question_db_stats["history_scores"].append([score/len(question_bank), f"{score}/{len(question_bank)}"])

    if calculated_score > question_db_stats["highest_score"]:
        question_db_stats["highest_score"] = calculated_score

    if len(incorrect_answers) > 0:
        print("\nWRONG ANSWERS:")
        for i in incorrect_answers:
            print(i)

    print(f"\nYou have scored {score} out of {len(question_bank)}.")


def view_questions():
    print("\n--- Question Bank ---")

    for i in range(len(question_db_main)):
        q = question_db_main[i]
        print(f"\nQuestion {i + 1}: {q["question"]}")
        print("Options:", q["options"])
        print("Answer:", q["answer"])
        print("Difficulty:", q["difficulty"])

def get_average_score():
    total = 0
    for i in range(len(question_db_stats["history_scores"])):
        total += question_db_stats["history_scores"][i][0]
    average_score = total / len(question_db_stats["history_scores"])
    return average_score

def view_statistics():
    print(question_db_stats["history_scores"])
    print(question_db_stats["highest_score"])
    print(str(get_average_score()))

def get_input_in_range(min_val, max_val):
    choice = -1
    valid_choice = False
    while valid_choice is not True:
        try:
            choice = int(input(f"Enter value in range {min_val} to {max_val}: "))
            if (type(choice) is int) & (min_val <= choice <= max_val):
                valid_choice = True

        except ValueError:
            print("Please enter a number")

    return choice

def get_difficulty_levels_from_qbank():
    difficulty_set = set()
    for question in question_db_main:
        difficulty_set.add(question["difficulty"])
    return list(difficulty_set)

def get_subjects_from_qbank():
    subjects_set = set()
    for question in question_db_main:
        subjects_set.add(question["subject"])
    return list(subjects_set)

def choose_quiz_details():
    subjects = get_subjects_from_qbank()
    difficulty_levels = get_difficulty_levels_from_qbank()

    print("Choose the subject: ")
    for i in range(len(subjects)):
        print(f"{i + 1}. {subjects[i].capitalize()}")
    subject_index = get_input_in_range(1, len(subjects)) - 1
    subject = subjects[subject_index]

    print("Choose the difficulty: ")
    for i in range(len(difficulty_levels)):
        print(f"{i + 1}. {difficulty_levels[i].capitalize()}")
    diff_index = get_input_in_range(1, len(difficulty_levels)) - 1
    difficulty = difficulty_levels[diff_index]

    return subject, difficulty

def main_menu():
    while True:
        print("\n=== WELCOME TO THE QUIZ MENU ===")
        print("1. Start Quiz")
        print("2. Look at Questions")
        print("3. Statistics")
        print("0. Exit")

        choice = get_input_in_range(0, 3)

        if choice == 1:
            subject, difficulty = choose_quiz_details()
            start_quiz(subject, difficulty)
        elif choice == 2:
            view_questions()
        elif choice == 3:
            view_statistics()
        elif choice == 0:
            print("Exit program.")
            break
        else:
            print("Wrong choice.")

main_menu()