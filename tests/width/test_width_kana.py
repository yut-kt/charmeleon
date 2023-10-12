"""Testcase for width.py."""
import unittest

from charmeleon import Width


class TestWidthKana(unittest.TestCase):
    """Testcase Katakana for width.py."""

    def setUp(self: "TestWidthKana") -> None:
        """Set up."""
        self.kana_true_widths = [
            ("only kana",
             Width(digit=False, alpha=False, punct=False, kana=True)),
            ("kana and digit",
             Width(digit=True, alpha=False, punct=False, kana=True)),
            ("kana and alpha",
             Width(digit=False, alpha=True, punct=False, kana=True)),
            ("kana and punct",
             Width(digit=False, alpha=False, punct=True, kana=True)),
            ("kana, digit and alpha",
             Width(digit=True, alpha=True, punct=False, kana=True)),
            ("kana, digit and punct",
             Width(digit=True, alpha=False, punct=True, kana=True)),
            ("kana, alpha and punct",
             Width(digit=False, alpha=True, punct=True, kana=True)),
        ]

        self.kana_false_widths = [
            ("only kana",
             Width(digit=True, alpha=True, punct=True, kana=False)),
            ("kana and digit",
             Width(digit=False, alpha=True, punct=True, kana=False)),
            ("kana and alpha",
             Width(digit=True, alpha=False, punct=True, kana=False)),
            ("kana and punct",
             Width(digit=True, alpha=True, punct=False, kana=False)),
            ("kana, digit and alpha",
             Width(digit=False, alpha=False, punct=True, kana=False)),
            ("kana, digit and punct",
             Width(digit=False, alpha=True, punct=False, kana=False)),
            ("kana, alpha and punct",
             Width(digit=True, alpha=False, punct=False, kana=False)),
        ]

        self.kana_half = ("ｱ ｲ ｳ ｴ ｵ ｶ ｷ ｸ ｹ ｺ ｻ ｼ ｽ ｾ ｿ ﾀ ﾁ ﾂ ﾃ ﾄ"
                          "ﾅ ﾆ ﾇ ﾈ ﾉ ﾊ ﾋ ﾌ ﾍ ﾎ ﾏ ﾐ ﾑ ﾒ ﾓ ﾔ ﾕ ﾖ"
                          "ﾗ ﾘ ﾙ ﾚ ﾛ ﾜ ｦ ﾝ"
                          "ｳﾞ ｶﾞ ｷﾞ ｸﾞ ｹﾞ ｺﾞ ｻﾞ ｼﾞ ｽﾞ ｾﾞ ｿﾞ ﾀﾞ ﾁﾞ ﾂﾞ ﾃﾞ ﾄﾞ"
                          "ﾊﾞ ﾋﾞ ﾌﾞ ﾍﾞ ﾎﾞ ﾊﾟ ﾋﾟ ﾌﾟ ﾍﾟ ﾎﾟ ｧ ｨ ｩ ｪ ｫ ｬ ｭ ｮ ｯ")

        self.kana_full = ("ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト"
                          "ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ"
                          "ラ リ ル レ ロ ワ ヲ ン"
                          "ヴ ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド"
                          "バ ビ ブ ベ ボ パ ピ プ ペ ポ ァ ィ ゥ ェ ォ ャ ュ ョ ッ")

    def test_kana_true_to_full(self: "TestWidthKana") -> None:
        """Test converting kana to full-width."""
        arg = self.kana_half
        expected = self.kana_full
        for name, width in self.kana_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_kana_false_to_full(self: "TestWidthKana") -> None:
        """Test converting kana to full-width."""
        arg = self.kana_half
        expected = self.kana_half
        for name, width in self.kana_false_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_full(arg))

    def test_kana_true_to_half(self: "TestWidthKana") -> None:
        """Test converting kana to half-width."""
        arg = self.kana_full
        expected = self.kana_half
        for name, width in self.kana_true_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))

    def test_kana_false_to_half(self: "TestWidthKana") -> None:
        """Test converting kana to half-width."""
        arg = self.kana_full
        expected = self.kana_full
        for name, width in self.kana_false_widths:
            with self.subTest(name=name):
                self.assertEqual(expected, width.to_half(arg))


if __name__ == "__main__":
    unittest.main()
