"""Testcase for width.py."""
import random
import unittest

from charmeleon import Width
from charmeleon.table import alpha, digit, kana, punct


class TestWidthAlpha(unittest.TestCase):
    """Testcase Alphabet for width.py."""

    def setUp(self: "TestWidthAlpha") -> None:
        """Set up."""
        self.width = Width(digit=True, alpha=True, punct=True, kana=True)
        self.half_full_tuples = list(digit.HALF2FULL.items()) + \
                                list(alpha.HALF2FULL.items()) + \
                                list(punct.HALF2FULL.items()) + \
                                [(h, f) for h, f in kana.HALF2FULL.items()
                                 if h not in (chr(0xFF9E), chr(0xFF9F))]

    def test_to_full(self: "TestWidthAlpha") -> None:
        """Test converting alpha to full-width."""
        for i in range(100):
            half_full_tuples = random.sample(self.half_full_tuples, 100)
            arg = "".join([half for half, full in half_full_tuples])
            expected = "".join([full for half, full in half_full_tuples])
            with self.subTest(name=f"for {i}"):
                self.assertEqual(expected, self.width.to_full(arg))

    def test_to_half(self: "TestWidthAlpha") -> None:
        """Test converting alpha to full-width."""
        for i in range(100):
            half_full_tuples = random.sample(self.half_full_tuples, 100)
            arg = "".join([full for half, full in half_full_tuples])
            expected = "".join([half for half, full in half_full_tuples])
            with self.subTest(name=f"for {i}"):
                self.assertEqual(expected, self.width.to_half(arg))


if __name__ == "__main__":
    unittest.main()
