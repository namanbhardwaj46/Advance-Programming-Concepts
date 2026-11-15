import unittest
from unittest.mock import patch
from config.imagePainter import divide_and_paint


class TestDivideAndPaint(unittest.TestCase):
    # Pending : Write one more thread to test the executor
    def test_output_correctness(self):
        matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        colors = ['red', 'blue', 'green', 'yellow']
        expected_output = [['red', 'red', 'blue', 'blue'],
                           ['red', 'red', 'blue', 'blue'],
                           ['green', 'green', 'yellow', 'yellow'],
                           ['green', 'green', 'yellow', 'yellow']]

        divide_and_paint(matrix, colors)

        # Check if the output matrix is painted correctly
        self.assertEqual(matrix, expected_output)


if __name__ == '__main__':
    unittest.main()