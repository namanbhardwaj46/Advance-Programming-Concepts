import unittest
import threading
from io import StringIO
import sys

from config.zeroEvenOdd import ZeroEvenOdd, PrintNumber


class TestZeroEvenOdd(unittest.TestCase):
    def execute_test_with_output(self, n, expected_output):
        """
        Executes the ZeroEvenOdd logic and captures the output.
        """
        # Temporary redirect stdout
        original_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            zeo = ZeroEvenOdd(n)
            pn = PrintNumber()

            def zero():
                zeo.zero(pn)

            def even():
                zeo.even(pn)

            def odd():
                zeo.odd(pn)

            threads = [
                threading.Thread(target=zero),
                threading.Thread(target=even),
                threading.Thread(target=odd)
            ]

            for t in threads:
                t.start()

            for t in threads:
                t.join()

            # Capture the output
            output_str = sys.stdout.getvalue()
        finally:
            # Ensure stdout is reset even if an exception occurs
            sys.stdout = original_stdout

        # Validate the captured output
        self.assertEqual(output_str, expected_output)

    def test_zero_even_odd(self):
        self.execute_test_with_output(5, "0102030405")


if __name__ == "__main__":
    unittest.main()
