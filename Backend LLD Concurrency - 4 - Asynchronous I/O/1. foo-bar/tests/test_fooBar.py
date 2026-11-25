import unittest
import threading
from io import StringIO
import sys

from config.fooBar import FooBar


class TestFooBar(unittest.TestCase):
    def setUp(self):
        # Save the original stdout so it can be restored after tests are done
        self.original_stdout = sys.stdout
        # Replace sys.stdout with a StringIO to capture the threads' output
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore the original stdout after each test case
        sys.stdout = self.original_stdout

    def test_foobar(self):
        n = 5
        fb = FooBar(n)

        def foo():
            fb.foo()

        def bar():
            fb.bar()

        threads = [threading.Thread(target=foo), threading.Thread(target=bar)]

        # Start the threads
        for t in threads:
            t.start()

        # Wait for the threads to complete
        for t in threads:
            t.join()

        # Now that the threads are done, capture and check the output
        output = sys.stdout.getvalue()  # Note: sys.stdout has been set to a StringIO object in setUp
        expected_output = 'foobar' * n

        # Reset sys.stdout to the original stdout before assertion (optional here since tearDown will handle it)
        sys.stdout = self.original_stdout

        # Assert the captured output against the expected output
        self.assertEqual(output.strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
