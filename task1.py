import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_answer):# this will ask the user the question
        print(f"\n{question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the corresponding number): ")#This will take the ans from the user and check if it is correct or not
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer = int(user_answer)
            if options[user_answer - 1] == correct_answer:
                print("Correct! Well done.")
                self.score += 1
            else:
                print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")
        else:
            print("Invalid input. Please enter a valid option.")

    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            self.ask_question(question, options, correct_answer)

        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")#Displaying the final score of the user

# The question set of the Quiz
quiz_questions = [
    ("What is the capital of France?", ["Berlin",  "Rome","Paris"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Mars","Venus","Jupiter"], "Mars"),
    ("What is the largest mammal on Earth?", ["Elephant", "Blue Whale", "Giraffe"], "Blue Whale"),
    ("What is the capital of Japan?",["Tokyo","Beijing","Seoul"], "Tokyo"),
    ('Who wrote "Romeo and Juliet"?',["Jane Austen","Charles Dickens","William Shakespeare"],"William Shakespeare"),
    ("What is the chemical symbol for gold?",["Ag","Au","Fe"],"Au")
]

# To Create and run the quiz
quiz = QuizGame(quiz_questions)
quiz.run_quiz()
