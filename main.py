import sys
from ai import AI

if len(sys.argv) < 2:
    sys.exit("Usage: python main.py <chava-file>")

ai = AI(
        model="gpt-4",
        temperature=0.1,
    )

with open(sys.argv[1], 'r') as file:
    chava_code = file.read()

ai.chat(chava_code)