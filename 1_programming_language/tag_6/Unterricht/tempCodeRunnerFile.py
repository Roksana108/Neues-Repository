# Gruppenarbeit: Trump-Parsen

from pathlib import Path
from pprint import pprint
import sys

user_input = list(input("Gebe einen Modus ein (SEN/ WORD/ TOP): ").split())
#  user_input_liste = list(user_input.strip(" "))
#  print(user_input[0], user_input[1])

comand = user_input[0]
term = user_input[1]

if len(user_input) != 2:
    print("Bitte gebe genau zwei Wörter ein.")
    sys.exit(0)

#  Einlesen mir read()

with open(Path(__file__).parent / "trump_speeches.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
    # print(content)

    content_sen = content.split(".")
    #  print("*" * 30)
    for sentence in content_sen:
        if term in sentence.split():
            print(sentence)