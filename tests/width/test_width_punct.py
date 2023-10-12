"""Testcase for width.py."""
import string
import unittest

from charmeleon import Width


class TestWidthPunct(unittest.TestCase):
    """Testcase Punctuation for width.py."""

    def setUp(self: "TestWidthPunct") -> None:
        """Set up."""
        self.punct_true_widths = [
            ("only punct",
             Width(digit=False, alpha=False, punct=True, kana=False)),
            ("punct and digit",
             Width(digit=True, alpha=False, punct=True, kana=False)),
            ("punct and alpha",
             Width(digit=False, alpha=True, punct=True, kana=False)),
            ("punct and kana",
             Width(digit=False, alpha=False, punct=True, kana=True)),
            ("punct, digit and alpha",
             Width(digit=True, alpha=True, punct=True, kana=False)),
            ("punct, digit and kana",
             Width(digit=True, alpha=False, punct=True, kana=True)),
            ("punct, alpha and kana",
             Width(digit=False, alpha=True, punct=True, kana=True)),
            ("all",
             Width(digit=True, alpha=True, punct=True, kana=True)),
        ]

        self.punct_false_widths = [
            ("only punct",
             Width(digit=True, alpha=True, punct=False, kana=True)),
            ("punct and digit",
             Width(digit=False, alpha=True, punct=False, kana=True)),
            ("punct and alpha",
             Width(digit=True, alpha=False, punct=False, kana=True)),
            ("punct and kana",
             Width(digit=True, alpha=True, punct=False, kana=False)),
            ("punct, digit and alpha",
             Width(digit=False, alpha=False, punct=False, kana=True)),
            ("punct, digit and kana",
             Width(digit=False, alpha=True, punct=False, kana=False)),
            ("punct, alpha and kana",
             Width(digit=True, alpha=False, punct=False, kana=False)),
        ]

    def test_punct_true_to_full(self: "TestWidthPunct") -> None:
        """Test converting punct to full-width."""
        arg = string.punctuation
        expected = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
        for name, width in self.punct_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_punct_false_to_full(self: "TestWidthPunct") -> None:
        """Test converting punct to full-width."""
        arg = string.punctuation
        expected = string.punctuation
        for name, width in self.punct_false_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_punct_true_to_half(self: "TestWidthPunct") -> None:
        """Test converting punct to half-width."""
        arg = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
        expected = string.punctuation
        for name, width in self.punct_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))

    def test_punct_false_to_half(self: "TestWidthPunct") -> None:
        """Test converting punct to half-width."""
        arg = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
        expected = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
        for name, width in self.punct_false_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))


if __name__ == "__main__":
    unittest.main()
