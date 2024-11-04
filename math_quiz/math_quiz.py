import random

def get_random_integer(min_val, max_val):
    """
    Get a random integer between min_val and max_val

    min_val (int): Minimum value for the random integer
    max_val (int): Maximum value for the random integer

    Returns:
    int: A random integer between min_value and max_val.
    """
    return random.randint(min_val, max_val)

def get_random_operator():
    """
    Randomly select a mathematical operator: +, -, or *.

    Returns:
        str: a string reprenting a mathematical operator.
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1, num2, operator):
    """
    Generate a math problem and calculate the expected answer based on operator.

    Parameters:
        num1 (int): the first operand in the operation
        num2 (int): the second operand in the operation
        operator (str): the operator for the problem (+, - or *)

    Returns:
        tuple: a tuple containing a string of the math problem and the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else: # operator =='*'
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Start a math quiz game, where the user answers simple arithmetic questions.
    """
    score = 0
    total_questions = 3 # total number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)
        operator = get_random_operator()

        problem, correct_answer=  generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
               print("Correct! You earned a point.")
               score +=1
            else:
               print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()