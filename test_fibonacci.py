import unittest

from main import fibonacci


class TestFibonacci(unittest.TestCase):
    numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
               987, 1597, 2584, 4181, 6765, 10946, 17711]

    def test_fibonacci(self):
        for index, number in enumerate(self.numbers):
            self.assertEqual(fibonacci(index + 1), number)


if __name__ == '__main__':
    unittest.main()
