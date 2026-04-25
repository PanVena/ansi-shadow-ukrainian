# ANSI Shadow Ukrainian (`ansi_shadow_ukr`)

Український варіант відомого FIGlet-шрифта **ANSI Shadow**, зроблений на основі
латинського оригіналу. Висота 9 рядків (на 2 більше за оригінальний 7-рядковий
ANSI Shadow), щоб лишити місце під діакритику українських літер (`Й`, `Ї`).
Покриває український абетковий набір — інших кириличних літер (російські,
сербські, тощо) у шрифті немає. Призначений для використання разом із
[pyfiglet](https://github.com/pwaller/pyfiglet).

> Ukrainian variant of the well-known **ANSI Shadow** FIGlet font, based on the
> Latin original. Height is 9 lines (vs. 7 in the original) to leave room for
> Ukrainian diacritics (`Й`, `Ї`). Covers the Ukrainian alphabet only — no
> other Cyrillic letters (Russian, Serbian, etc.) are included. For use with
> [pyfiglet](https://github.com/pwaller/pyfiglet).

## Файли / Files

- `ansi_shadow_ukr.flf` — сам шрифт у форматі FIGlet.
- `install.py` — копіює шрифт у теку `pyfiglet/fonts/` встановленого pyfiglet.
- `demo.py` — рендерить рядок цим шрифтом без постійної інсталяції.

## Встановлення / Installation

```bash
pip install pyfiglet
python install.py
```

Перевір:

```bash
pyfiglet -f ansi_shadow_ukr "Привіт"
```

Видалити з pyfiglet:

```bash
python install.py --uninstall
```

## Використання у власному коді / Use in your own code

```python
import pyfiglet

# Варіант A: одноразово прокинути .flf у pyfiglet (ідемпотентно;
# фактично інсталює шрифт, але не вимагає попередньо запускати install.py)
pyfiglet.FigletFont.installFonts("ansi_shadow_ukr.flf")
print(pyfiglet.Figlet(font="ansi_shadow_ukr").renderText("Привіт"))

# Варіант B: після `python install.py` — як зі звичайним вбудованим шрифтом
print(pyfiglet.figlet_format("Привіт", font="ansi_shadow_ukr"))
```

## Покриття / Coverage

Латиниця (як в оригіналі ANSI Shadow), український алфавіт (`А-Я`, `Ґ`, `Є`,
`І`, `Ї` та їхні строкові форми), цифри й базова пунктуація. Російські /
сербські / болгарські літери (`Ё`, `Ы`, `Ъ`, `Э`, `Ђ`, `Ј` тощо) **не
включені**.

## Ліцензія / License

Цей український варіант поширюється за ліцензією **MIT** (див. [LICENSE](LICENSE)).
Базовий малюнок гліфів ANSI Shadow походить зі спільнотного FIGlet/TheDraw
сімейства, де автор оригіналу не задокументований
(`Font Author: ?` у вихідному `.flf`).

> This Ukrainian variant is distributed under the **MIT License** (see
> [LICENSE](LICENSE)). The underlying ANSI Shadow glyph design comes from the
> community FIGlet/TheDraw font family; the original author is undocumented
> (`Font Author: ?` in the source `.flf`).

## Автор української адаптації / Ukrainian adaptation author

Pan Vena (Ліниві ШІ / Lazy AIs), 2026.

Використовується у грі *Dungeon Revizor: The Game*.
