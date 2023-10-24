"""Testcase for width.py."""
import random
import unittest

from charmeleon import Width
from charmeleon.error import ArgError
from charmeleon.table import alpha, digit, kana, punct


class TestWidth(unittest.TestCase):
    """Testcase Alphabet for width.py."""

    def setUp(self: "TestWidth") -> None:
        """Set up."""
        self.width = Width(go=True)
        self.half_full_tuples = list(digit.HALF2FULL.items()) + \
                                list(alpha.HALF2FULL.items()) + \
                                list(punct.HALF2FULL.items()) + \
                                [(h, f) for h, f in kana.HALF2FULL.items()
                                 if h not in (chr(0xFF9E), chr(0xFF9F))]

    def test_to_full(self: "TestWidth") -> None:
        """Test converting alpha to full-width."""
        for i in range(100):
            half_full_tuples = random.sample(self.half_full_tuples, 100)
            arg = "".join([half for half, full in half_full_tuples])
            expected = "".join([full for half, full in half_full_tuples])
            with self.subTest(name=f"for {i}"):
                self.assertEqual(expected, self.width.to_full(arg))

    def test_to_half(self: "TestWidth") -> None:
        """Test converting alpha to full-width."""
        for i in range(100):
            half_full_tuples = random.sample(self.half_full_tuples, 100)
            arg = "".join([full for half, full in half_full_tuples])
            expected = "".join([half for half, full in half_full_tuples])
            with self.subTest(name=f"for {i}"):
                self.assertEqual(expected, self.width.to_half(arg))

    def test_fail_init(self: "TestWidth") -> None:
        """Test fail init."""
        with self.assertRaises(ArgError):
            Width(digit=False, alpha=False, punct=False, kana=False)

    def test_narrow(self: "TestWidth") -> None:
        """Test golang narrow."""
        self.assertEqual("abｦ₩￮¥A", self.width.narrow("abヲ￦○￥Ａ"))

    def test_widen(self: "TestWidth") -> None:
        """Test golang widen."""
        self.assertEqual("ａｂ￥ヲ￦○", self.width.widen("ab¥ｦ₩￮"))

    def test_fold(self: "TestWidth") -> None:
        """Test golang fold."""
        self.assertEqual("abヲ₩○¥A", self.width.fold("abｦ￦￮￥Ａ"))
