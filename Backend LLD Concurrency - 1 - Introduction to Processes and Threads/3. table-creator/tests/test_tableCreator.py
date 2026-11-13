import unittest
from unittest.mock import patch
from io import StringIO
from config.tableCreator import TableCreator


class TestTableCreator(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_creation_for_3(self, mock_stdout):
        expected_output = "".join([f"3 times {i} is {3 * i}\n" for i in range(1, 11)])
        TableCreator(3).run()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_creation_for_large_number(self, mock_stdout):
        number = 20
        expected_output = "".join([f"{number} times {i} is {number * i}\n" for i in range(1, 11)])
        TableCreator(number).run()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_creation_for_1(self, mock_stdout):
        expected_output = "".join([f"1 times {i} is {i}\n" for i in range(1, 11)])
        TableCreator(1).run()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_creation_for_0(self, mock_stdout):
        expected_output = "".join([f"0 times {i} is 0\n" for i in range(1, 11)])
        TableCreator(0).run()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_table_creation_for_negative_number(self, mock_stdout):
        number = -3
        expected_output = "".join([f"-3 times {i} is {-3 * i}\n" for i in range(1, 11)])
        TableCreator(number).run()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Additional concurrency test may require a more complex setup,
    # including asserting the concurrency behavior or output order.


if __name__ == "__main__":
    unittest.main()
