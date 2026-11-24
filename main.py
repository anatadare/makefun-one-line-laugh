"""The One-Line Laugh entry.

The joke: a phone charger that only works at one exact angle forces
you to sleep contorted around it, so the chiropractor bills it as
a cry for help. Relatable tech pain, one line, 135 characters.
"""

import os

LINE = "My charger only works at one exact angle, so every night my phone and I fall asleep in a position my chiropractor calls a cry for help."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
