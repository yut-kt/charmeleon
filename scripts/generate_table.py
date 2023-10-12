"""Generate char tables."""
import pathlib
from unicodedata import normalize

from jinja2 import Environment, FileSystemLoader


def main() -> None:
    """Process Main function."""
    table_path = pathlib.Path("../charmeleon/table")

    j2_env = Environment(loader=FileSystemLoader(table_path / "template"))
    j2_env.filters = {"py_str": py_str}

    chars_dict = get_chars_dict()
    for template_file in j2_env.list_templates():
        template = j2_env.get_template(template_file)
        py_src = template.render(chars_dict)
        py_file = pathlib.Path(template_file).stem
        with (table_path / py_file).open("w") as f:
            f.write(py_src)


def get_chars_dict() -> dict:
    """Char dict."""
    return {
        "ascii_half_chars": [chr(0x0021 + i) for i in range(94)],
        "ascii_full_chars": [chr(0xFF01 + i) for i in range(94)],
        "digit_half_chars": [chr(0x0030 + i) for i in range(10)],
        "digit_full_chars": [chr(0xFF10 + i) for i in range(10)],
        "alpha_half_chars": [chr(0x0041 + i) for i in range(26)] +
                            [chr(0x0061 + i) for i in range(26)],
        "alpha_full_chars": [chr(0xFF21 + i) for i in range(26)] +
                            [chr(0xFF41 + i) for i in range(26)],
        "punct_half_chars": [chr(0x0021 + i) for i in range(15)] +
                            [chr(0x003A + i) for i in range(7)] +
                            [chr(0x005B + i) for i in range(6)] +
                            [chr(0x007B + i) for i in range(4)],
        "punct_full_chars": [chr(0xFF01 + i) for i in range(15)] +
                            [chr(0xFF1A + i) for i in range(7)] +
                            [chr(0xFF3B + i) for i in range(6)] +
                            [chr(0xFF5B + i) for i in range(4)],
        "kana_half_chars":
            [chr(0xFF61 + i) + chr(0xFF9E) for i in range(63)
             if len(normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9E))) == 1] +
            [chr(0xFF61 + i) + chr(0xFF9F) for i in range(63)
             if len(normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9F))) == 1] +
            [chr(0xFF61 + i) for i in range(63)],
        "kana_full_chars":
            [normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9E)) for i in range(63)
             if len(normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9E))) == 1] +
            [normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9F)) for i in range(63)
             if len(normalize("NFKC", chr(0xFF61 + i) + chr(0xFF9F))) == 1] +
            [normalize("NFKC", chr(0xFF61 + i)) for i in range(63)],
    }


def py_str(char: str) -> str:
    """特定の文字だけをエスケープする関数."""
    # 特定の文字だけをエスケープするロジックを書く
    if char == "\\":
        return '"\\' + char + '"'
    if char == '"':
        return "'" + char + "'"
    return '"' + char + '"'


if __name__ == "__main__":
    main()
