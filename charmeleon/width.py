"""Width class for handling width of characters."""
import re

import charmeleon.table.alpha
import charmeleon.table.digit
import charmeleon.table.kana
import charmeleon.table.punct
from charmeleon.error import ArgError


class Width:
    """Width class for handling width of characters."""

    def __init__(self: "Width",
                 digit: bool = True,
                 alpha: bool = True,
                 punct: bool = True,
                 kana: bool = True) -> None:
        """
        Initialize Width class.

        Args:
        ----
            digit (bool): True if digit characters are used.
            alpha (bool): True if alphabet characters are used.
            punct (bool): True if punctuation characters are used.
            kana (bool): True if kana characters are used.

        Raises:
        ------
            ArgError: If all of digit, alpha, punct and kana are False.
        """
        if not any({digit, alpha, punct, kana}):
            msg = "At least one of digit, alpha, punct or kana must be True."
            raise ArgError(msg)
        self.__h2f_table = {}
        self.__f2h_table = {}
        self.__hs2f_pattern = None
        if digit:
            self.__h2f_table |= str.maketrans(charmeleon.table.digit.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.digit.FULL2HALF)
        if alpha:
            self.__h2f_table |= str.maketrans(charmeleon.table.alpha.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.alpha.FULL2HALF)
        if punct:
            self.__h2f_table |= str.maketrans(charmeleon.table.punct.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.punct.FULL2HALF)
        if kana:
            self.__h2f_table |= str.maketrans(charmeleon.table.kana.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.kana.FULL2HALF)
            self.__hs2f = charmeleon.table.kana.HALFS2FULL
            self.__hs2f_pattern = re.compile(
                "|".join(map(re.escape, self.__hs2f.keys())))

    def __h2f_replace(self: "Width", match: re.Match) -> str:
        """Replace function for re.sub."""
        return self.__hs2f[match.group(0)]

    def to_full(self: "Width", chars: str) -> str:
        """
        Convert half-width characters to full-width characters.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width()
            >>> width.to_full("abc")
            'ａｂｃ'
        """
        if self.__hs2f_pattern:
            return (self.__hs2f_pattern.sub(self.__h2f_replace, chars)
                    .translate(self.__h2f_table))
        return chars.translate(self.__h2f_table)

    def to_half(self: "Width", chars: str) -> str:
        """
        Convert full-width characters to half-width characters.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width()
            >>> width.to_half("ＡＢＣ")
            'ABC'
        """
        return chars.translate(self.__f2h_table)
