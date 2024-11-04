import unittest
from math_quiz import get_random_integer, get_random_operator, generate_problem_and_answer

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
            pass

    def test_random_operator(self):
        # Check that the operator generated ie one of the expected operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test multiple random generations
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)
            pass

    def test_generate_problem_and_answer(self):
            # Test cases for different operators and numbers
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '-', '6 - 3', 3),
                (8, 5, '*', '8 * 5', 40),
                (10, 0, '*', '10 * 0', 0),
                (0, 0, '+', '0 + 0', 0),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem_and_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
