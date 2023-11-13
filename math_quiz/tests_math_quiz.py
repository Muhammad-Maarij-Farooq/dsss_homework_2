import unittest
from math_quiz import function_X, function_Y, function_Z

class TestMathGame(unittest.TestCase):

    def test_function_X(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_X(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_Y(self):
        # Test if function_Y returns one of the expected operators
        operators = ['+', '-', '*']
        for _ in range(1000):
            operator = function_Y()
            self.assertIn(operator, operators)

    def test_function_Z(self):
        # Test if function_Z returns the correct problem and answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 3, '*', '4 * 3', 12)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_Z(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
