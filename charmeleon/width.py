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
        """Initialize Width class."""
        if not any({digit, alpha, punct, kana}):
            msg = "At least one of digit, alpha, punct or kana must be True."
            raise ArgError(msg)
        self.__h2f = {}
        self.__f2h = {}
        if digit:
            self.__h2f |= charmeleon.table.digit.HALF2FULL
            self.__f2h |= charmeleon.table.digit.FULL2HALF
        if alpha:
            self.__h2f |= charmeleon.table.alpha.HALF2FULL
            self.__f2h |= charmeleon.table.alpha.FULL2HALF
        if punct:
            self.__h2f |= charmeleon.table.punct.HALF2FULL
            self.__f2h |= charmeleon.table.punct.FULL2HALF
        if kana:
            self.__h2f |= charmeleon.table.kana.HALF2FULL
            self.__f2h |= charmeleon.table.kana.FULL2HALF
        self.__h2f_pattern = re.compile("|".join(map(re.escape, self.__h2f.keys())))
        self.__f2h_pattern = re.compile("|".join(map(re.escape, self.__f2h.keys())))


    def __h2f_replace(self: "Width", match: re.Match) -> str:
        """Replace function for re.sub."""
        return self.__h2f[match.group(0)]

    def __f2h_replace(self: "Width", match: re.Match) -> str:
        """Replace function for re.sub."""
        return self.__f2h[match.group(0)]

    def to_full(self: "Width", chars: str) -> str:
        """Convert half-width characters to full-width characters."""
        return self.__h2f_pattern.sub(self.__h2f_replace, chars)

    def to_half(self: "Width", chars: str) -> str:
        """Convert full-width characters to half-width characters."""
        return self.__f2h_pattern.sub(self.__f2h_replace, chars)
