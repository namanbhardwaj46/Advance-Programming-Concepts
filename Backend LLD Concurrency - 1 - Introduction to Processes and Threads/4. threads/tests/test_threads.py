import sys
import unittest
from io import StringIO

# Assuming your classes are correctly imported from the config.threads module
from config.threads import Adder, Subtractor, Client


class TestClient(unittest.TestCase):
    def setUp(self):
        # Save the original sys.stdout to restore it later
        self.original_stdout = sys.stdout
        # Redirect sys.stdout to a StringIO object to capture the outputs
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset sys.stdout to its original state
        sys.stdout = self.original_stdout

    def test_adder_output(self):
        Adder().run()
        # After running Adder, capture its output
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "I am the Adder class")

    def test_subtractor_output(self):
        # Clear the current StringIO buffer before the next test
        sys.stdout.seek(0)
        sys.stdout.truncate()

        Subtractor().run()
        # After running Subtractor, capture its output
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "I am the Subtractor class")

    def test_main_output(self):
        # Clear the current StringIO buffer before the next test
        sys.stdout.seek(0)
        sys.stdout.truncate()

        Client.main()
        # After running Client.main(), capture its output
        output = sys.stdout.getvalue().strip()
        # Check if the output matches the expected sequence of statements
        expected_output = "I am the main class\nI am the Adder class\nI am the Subtractor class"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
