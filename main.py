import sys
from ai import AI

if len(sys.argv) < 2:
    sys.exit("Usage: python main.py <chava-file>")

ai = AI(
        model="gpt-4",
        temperature=0,
    )

with open(sys.argv[1], 'r', encoding="utf8") as file:
    chava_code = file.read()

ai.chat(sys.argv[1], chava_code)