import unittest
from examples.recursion import factorial_recursive, factorial_iterative

class RecursionTests(unittest.TestCase):
    def test_match(self):
        for n in range(8):
            self.assertEqual(factorial_recursive(n), factorial_iterative(n))
    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)

if __name__ == "__main__":
    unittest.main()
