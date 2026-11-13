import math
import unittest

from config.factorial import compute_large_factorial


class TestFactorialThread(unittest.TestCase):
    def test_thread_used(self):
        """Test to ensure that a thread is used and it returns a valid integer result for large numbers."""
        n = 1000
        result = compute_large_factorial(n)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, int))
        self.assertTrue(result > 0)

    def test_result_small_number(self):
        """Test to ensure the factorial result is correct for a small number."""
        n = 5
        result = compute_large_factorial(n)
        self.assertEqual(result, math.factorial(n))

    def test_result_large_number(self):
        """Test to ensure the factorial result is correct for a large number."""
        n = 20
        result = compute_large_factorial(n)
        self.assertEqual(result, math.factorial(n))

    def test_result_zero(self):
        """Test to ensure the factorial of 0 is 1."""
        n = 0
        result = compute_large_factorial(n)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
