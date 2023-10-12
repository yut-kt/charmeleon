"""Testcase for width.py."""
import unittest

from charmeleon import Width


class TestWidthAlpha(unittest.TestCase):
    """Testcase Alphabet for width.py."""

    def setUp(self: "TestWidthAlpha") -> None:
        """Set up."""
        self.alpha_true_widths = [
            ("only alpha",
             Width(digit=False, alpha=True, punct=False, kana=False)),
            ("alpha and digit",
             Width(digit=True, alpha=True, punct=False, kana=False)),
            ("alpha and punct",
             Width(digit=False, alpha=True, punct=True, kana=False)),
            ("alpha and kana",
             Width(digit=False, alpha=True, punct=False, kana=True)),
            ("alpha, digit and punct",
             Width(digit=True, alpha=True, punct=True, kana=False)),
            ("alpha, digit and kana",
             Width(digit=True, alpha=True, punct=False, kana=True)),
            ("alpha, punct and kana",
             Width(digit=False, alpha=True, punct=True, kana=True)),
            ("all",
             Width(digit=True, alpha=True, punct=True, kana=True)),
        ]

        self.alpha_false_width = [
            ("only alpha",
             Width(digit=True, alpha=False, punct=True, kana=True)),
            ("alpha and digit",
             Width(digit=False, alpha=False, punct=True, kana=True)),
            ("alpha and punct",
             Width(digit=True, alpha=False, punct=False, kana=True)),
            ("alpha and kana",
             Width(digit=True, alpha=False, punct=True, kana=False)),
            ("alpha, digit and punct",
             Width(digit=False, alpha=False, punct=False, kana=True)),
            ("alpha, digit and kana",
             Width(digit=False, alpha=False, punct=True, kana=False)),
            ("alpha, punct and kana",
             Width(digit=True, alpha=False, punct=False, kana=False)),
        ]

    def test_alpha_true_to_full(self: "TestWidthAlpha") -> None:
        """Test converting alpha to full-width."""
        arg = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        expected = ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
                    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
        for name, width in self.alpha_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_alpha_false_to_full(self: "TestWidthAlpha") -> None:
        """Test converting alpha to full-width."""
        arg = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for name, width in self.alpha_false_width:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_alpha_true_to_half(self: "TestWidthAlpha") -> None:
        """Test converting alpha to half-width."""
        arg = ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
               "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
        expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        for name, width in self.alpha_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))

    def test_alpha_false_to_half(self: "TestWidthAlpha") -> None:
        """Test converting alpha to half-width."""
        arg = ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
               "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
        expected = ("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
                    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")
        for name, width in self.alpha_false_width:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))


if __name__ == "__main__":
    unittest.main()
