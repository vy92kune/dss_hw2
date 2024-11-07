import random

def generate_problem():
    """Generates a random math problem and its answer."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 5)
    operator = random.choice(['+', '-', '*'])

    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem, answer

def math_quiz(num_questions=10):
    """Conducts a math quiz with the specified number of questions."""
    score = 0

    print("Welcome to the Math Quiz!")
    print("Solve the math problems and enter your answers.")

    for _ in range(num_questions):
        problem, answer = generate_problem()
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is {answer}.")

    print(f"\nQuiz over! Your score is: {score}/{num_questions}")

if __name__ == "__main__":
    math_quiz()
