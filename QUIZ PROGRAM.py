#quiz_program.py

def run_quiz(questions):
    score = 0
    print(" Welcome to the Ultimate Python Quiz!")
    print("--------------------------------------\n")

    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == question["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question['answer']}\n")

    print(f" You got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print(" You're a Python master!")
    elif score >= len(questions) // 2:
        print(" Not bad! Keep sharpening your skills.")
    else:
        print(" Keep learning. You're on the path!")

# List of questions
quiz_questions = [
    {
        "question": "1. What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A. def", "B. func", "C. function", "D. define"],
        "answer": "A"
    },
    {
        "question": "3. What does the 'len()' function do?",
        "options": ["A. Returns a random number", "B. Returns the size of a list", "C. Converts data type", "D. Creates a loop"],
        "answer": "B"
    },
    {
        "question": "4. What is the output of: print('Hello' + 'World')?",
        "options": ["A. Hello World", "B. Hello+World", "C. HelloWorld", "D. Error"],
        "answer": "C"
    },
    {
        "question": "5. Which of the following is a correct variable name?",
        "options": ["A. 1name", "B. name_1", "C. name-1", "D. name 1"],
        "answer": "B"
    }
]

# Run the quiz
if __name__ == "__main__":
    run_quiz(quiz_questions)
