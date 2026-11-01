import unittest
from examples.algorithms import linear_search, binary_search, count_frequencies

class AlgorithmTests(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(linear_search([4, 8, 2], 8), 1)
        self.assertEqual(linear_search([4, 8, 2], 9), -1)
    def test_binary(self):
        self.assertEqual(binary_search([1, 3, 5, 7], 1), 0)
        self.assertEqual(binary_search([1, 3, 5, 7], 7), 3)
        self.assertEqual(binary_search([], 2), -1)
    def test_frequency(self):
        self.assertEqual(count_frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

if __name__ == "__main__":
    unittest.main()
