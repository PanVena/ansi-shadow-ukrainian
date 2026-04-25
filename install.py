"""Копіює ansi_shadow_ukr.flf у теку шрифтів встановленого pyfiglet,
щоб шрифт був доступний як звичайний (наприклад: pyfiglet -f ansi_shadow_ukr "Привіт").

Використання:
    python install.py            # встановити
    python install.py --uninstall # видалити з pyfiglet

Copies ansi_shadow_ukr.flf into the installed pyfiglet fonts directory so
the font becomes available like any other (e.g. `pyfiglet -f ansi_shadow_ukr "Hello"`).
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys


FONT_FILENAME = "ansi_shadow_ukr.flf"


def _pyfiglet_fonts_dir() -> str:
    try:
        import pyfiglet  # noqa: F401
    except ImportError:
        sys.exit("pyfiglet не встановлено. Спершу: pip install pyfiglet")

    try:
        from importlib.resources import files
        return str(files("pyfiglet.fonts"))
    except Exception:
        import pyfiglet
        return os.path.join(os.path.dirname(pyfiglet.__file__), "fonts")


def install() -> None:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), FONT_FILENAME)
    if not os.path.isfile(src):
        sys.exit(f"Не знайдено шрифт: {src}")
    dst_dir = _pyfiglet_fonts_dir()
    dst = os.path.join(dst_dir, FONT_FILENAME)
    shutil.copy2(src, dst)
    print(f"Встановлено: {dst}")
    print('Перевір: pyfiglet -f ansi_shadow_ukr "Привіт"')


def uninstall() -> None:
    dst = os.path.join(_pyfiglet_fonts_dir(), FONT_FILENAME)
    if os.path.isfile(dst):
        os.remove(dst)
        print(f"Видалено: {dst}")
    else:
        print(f"Файла нема: {dst}")


def main() -> None:
    p = argparse.ArgumentParser(description="Install/uninstall ansi_shadow_ukr font for pyfiglet.")
    p.add_argument("--uninstall", action="store_true", help="Remove the font from pyfiglet.")
    args = p.parse_args()
    (uninstall if args.uninstall else install)()


if __name__ == "__main__":
    main()
