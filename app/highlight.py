# -*- coding: utf-8 -*-


def highlight(string, color):
    """return colorized string for printing to terminal."""
    color_mapping = {
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "purple": "35",
    }
    if color not in color_mapping:
        return string
    else:
        attr = color_mapping[color]
        return f"\x1b[{attr}m{string}\x1b[0m"
