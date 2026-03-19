quizquestions = [
    {
    "question":"What is 1+1?",
    "answer":"2",
    "hint":"Add the two numbers together",
    }, {
    "question":"What is 5*2?",
    "answer":"10",
    "hint":"Multiply the two numbers together",
    }, {
    "question":"What is 3-2?",
    "answer":"1",
    "hint":"Subtract the two numbers together",
    }
]

def ask_question(q):
    print(q["question"])
    while True:
        user_input = input("Answer: ")
        if user_input == "hint":
            print(q["hint"])
        elif user_input == q["answer"]:
            print("Correct")
            return True
        else:
            print("Wrong. The answer was ", q["answer"])
            return False

def run_quiz(questions):
    score = 0
    for question in questions:
        if ask_question(question):
            score+=1
    print("Your score is ", score, "/", len(questions))
    percentage = score / len(questions) * 100
    if percentage == 100:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__ == "__main__":
    print("1. Full quiz")
    print("2. Quit")
    choice = input("Choose: ")
    if choice == "1":
        run_quiz(quizquestions)
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid Choice")