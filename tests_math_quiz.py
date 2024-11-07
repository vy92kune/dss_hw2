class TestMathQuiz(unittest.TestCase):

    def test_generate_math_problem(self):
        """Test that generate_math_problem returns a string and an integer."""
        problem, solution = generate_math_problem()
        self.assertIsInstance(problem, str)
        self.assertIsInstance(solution, int)

    @patch('builtins.input', side_effect=['3', '5', '7', '9'])
    @patch('random.randint', side_effect=[1, 2, 2, 3, 3, 4, 4, 5])  # Control numbers for predictability
    @patch('random.choice', side_effect=['+', '+', '+', '+'])  # Control operators for predictability
    def test_correct_answers(self, mock_input, mock_randint, mock_choice):
        """Test the quiz with all correct answers."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            score = conduct_math_quiz(4)
        self.assertEqual(score, 4)

    @patch('builtins.input', side_effect=['0', '0', '0', '0'])
    @patch('random.randint', side_effect=[1, 2, 2, 3, 3, 4, 4, 5])
    @patch('random.choice', side_effect=['+', '+', '+', '+'])
    def test_incorrect_answers(self, mock_input, mock_randint, mock_choice):
        """Test the quiz with all incorrect answers."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            score = conduct_math_quiz(4)
        self.assertEqual(score, 0)

    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd'])
    @patch('random.randint', side_effect=[1, 2, 2, 3, 3, 4, 4, 5])
    @patch('random.choice', side_effect=['+', '+', '+', '+'])
    def test_invalid_input(self, mock_input, mock_randint, mock_choice):
        """Test the quiz with invalid inputs."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            score = conduct_math_quiz(4)
            self.assertIn("Invalid input. Please enter a number.", fake_out.getvalue())

if _name_ == "_main_":
    unittest.main()
