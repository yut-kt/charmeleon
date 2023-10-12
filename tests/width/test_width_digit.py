"""Testcase for width.py."""
import unittest

from charmeleon import Width


class TestWidthDigit(unittest.TestCase):
    """Testcase Digit for width.py."""

    def setUp(self: "TestWidthDigit") -> None:
        """Set up."""
        self.digit_true_widths = [
            ("only digit",
             Width(digit=True, alpha=False, punct=False, kana=False)),
            ("digit and alpha",
             Width(digit=True, alpha=True, punct=False, kana=False)),
            ("digit and punct",
             Width(digit=True, alpha=False, punct=True, kana=False)),
            ("digit and kana",
             Width(digit=True, alpha=False, punct=False, kana=True)),
            ("digit, alpha and punct",
             Width(digit=True, alpha=True, punct=True, kana=False)),
            ("digit, alpha and kana",
             Width(digit=True, alpha=True, punct=False, kana=True)),
            ("digit, punct and kana",
             Width(digit=True, alpha=False, punct=True, kana=True)),
        ]

        self.digit_false_widths = [
            ("only digit",
             Width(digit=False, alpha=True, punct=True, kana=True)),
            ("digit and alpha",
             Width(digit=False, alpha=False, punct=True, kana=True)),
            ("digit and punct",
             Width(digit=False, alpha=True, punct=False, kana=True)),
            ("digit and kana",
             Width(digit=False, alpha=True, punct=True, kana=False)),
            ("digit, alpha and punct",
             Width(digit=False, alpha=False, punct=False, kana=True)),
            ("digit, alpha and kana",
             Width(digit=False, alpha=False, punct=True, kana=False)),
            ("digit, punct and kana",
             Width(digit=False, alpha=True, punct=False, kana=False)),
        ]

    def test_digit_true_to_full(self: "TestWidthDigit") -> None:
        """Test converting digit to full-width."""
        arg = "0123456789"
        expected = "０１２３４５６７８９"
        for name, width in self.digit_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_digit_false_to_full(self: "TestWidthDigit") -> None:
        """Test converting digit to full-width."""
        arg = "0123456789"
        for name, width in self.digit_false_widths:
            with self.subTest(name=name):
                width.to_full(arg)

    def test_digit_true_to_half(self: "TestWidthDigit") -> None:
        """Test converting digit to half-width."""
        arg = "０１２３４５６７８９"
        expected = "0123456789"
        for name, width in self.digit_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))

    def test_digit_false_to_half(self: "TestWidthDigit") -> None:
        """Test converting digit to half-width."""
        arg = "０１２３４５６７８９"
        expected = "０１２３４５６７８９"
        for name, width in self.digit_false_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))


if __name__ == "__main__":
    unittest.main()
