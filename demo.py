"""Швидке демо шрифта ansi_shadow_ukr.

Викликай:
    python demo.py             # стандартне слово
    python demo.py "Привіт!"   # власний текст

Викликає pyfiglet.FigletFont.installFonts() — це копіює .flf у теку
pyfiglet (тож фактично інсталює шрифт; окремий запуск install.py не
потрібен). Виклик ідемпотентний.
"""

from __future__ import annotations

import os
import sys

import pyfiglet


FONT_FILENAME = "ansi_shadow_ukr.flf"


def main() -> None:
    text = sys.argv[1] if len(sys.argv) > 1 else "Привіт, світе!"
    here = os.path.dirname(os.path.abspath(__file__))
    flf_path = os.path.join(here, FONT_FILENAME)

    pyfiglet.FigletFont.installFonts(flf_path)
    fig = pyfiglet.Figlet(font="ansi_shadow_ukr", width=200)
    print(fig.renderText(text))


if __name__ == "__main__":
    main()
