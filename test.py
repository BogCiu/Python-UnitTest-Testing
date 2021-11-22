import unittest
import main


class TestMain(unittest.TestCase):
    def test_function_test(self):
        test_argument = [1, 3, 5, 9, "E", "E"]
        result = main.function_test(test_argument)
        self.assertEqual(result, [1, 3])

    def test2_function_test(self):
        test_argument = []
        result = main.function_test(test_argument)
        self.assertEqual(result, [])

    def test3_function_test(self):
        test_argument = [9, 1, 'E', -5, 4, 7, 2, -9, -1, -4, 8, 'E', 'E', 6, 'E', 3, 0, 'E', -8, -7, 'E', 5, 10, 'E',
                         -3, -2, -6]
        result = main.function_test(test_argument)
        self.assertEqual(result, [1, -9, -5, -4, -1, -8, -7])


unittest.main()
