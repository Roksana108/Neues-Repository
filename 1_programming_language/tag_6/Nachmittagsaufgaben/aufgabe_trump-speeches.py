"""
Gruppenarbeit: Trump-Parser
"""
from pathlib import Path
import sys
import operator

# Einlesen der Text-Datei mit read()
with open(Path(__file__).parent / "trump_speeches.txt", mode="r", encoding="utf-8") as f:
    content = f.read()
    # print(content)

user_input = input("Gebe einen Modus ein (SEN/ WORD/ TOP): ").split()   # .split() hat Rückgabewert ist Liste
command = user_input[0]

# Prüfe die richtige Eingabe
if len(user_input) != 2:
    if command.upper() == "TOP":
        # Erstelle die Wörterliste
        content_words = content.split()
        word_count = {}
        topten_word_count = []

        print("*" * 30)
        # Bereinige alle Wörter von Satzzeichen, zähle alle Wörter der Länge >=5, speichere sie in eine dictionary
        for word in content_words:
            word_stripped = word.strip("/&%$§.,;:?!-[]\"")
            if len(word_stripped) >= 5:
                word_stripped = word_stripped.lower()                
                if word_stripped in word_count:
                    word_count[word_stripped] += 1      
                else:
                    word_count[word_stripped] = 1
        # print(word_count)
        # Sortiere die Tupel in der dictionary nach dem zweiten Eintrag
        sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=False)
        # Erstelle die TOP-TEN Liste
        for i in range(10):
            # .pop() löscht das letzte Element aus der sorted_word_count-Liste und fügt es in die topten_word_count-Liste ein
            topten_word_count.append(sorted_word_count.pop()) 
        print("TOP-TEN Wortliste = ", topten_word_count)
        print("*" * 30)
    else:
        print("Bitte geben Sie genau zwei Wörter ein.")
        sys.exit(0)
else:
    term = user_input[1]

    if command.upper() == "SEN":
        # Erstelle eine Liste mit den einzelnen Sätzen als Einträge
        content_sen = content.split(".")
        print("*" * 30)
        # Prüfe, ob das eingegebene Wort in den einzelnen Sätzen enthalten ist bzw. vorkommt
        for sentence in content_sen:
            if term in sentence.split():        # .split() teilt die Sätze in einzelne Wörter
                print(sentence + ".\n")
        print("*" * 30)

    if command.upper() == "WORD":
        # Erstelle die Wörterliste
        content_words = content.split()
        word_list = []
        print("*" * 30)
        # Prüfe, ob die eingegebene Buchstabenkombination in den Wörtern enthalten ist bzw. vorkommt
        # Füge die von Satzzeichen bereinigten Wörter in eine neue Wörterliste, in der jedes Wort nur einmal vorkommt
        for word in content_words:
            if term in word:
                if word.strip("/&%$§.,;:?!-[]\"") not in word_list:
                    word_list.append(word.strip("/&%$§.,;:?!-[]\""))
        # Sortiere die Wörterliste
        word_list.sort(reverse=False)
        print(word_list)
        print("*" * 30)
