# Donald was here, maybe also Melania.
from pathlib import Path


user_input = input("""Bitte Modus und Suchwort angeben.
SEN  suchwort  : sucht nach Sätzen mit suchwort.
WORD suchwort  : sucht nach Wörtern mot suchwort als Teilwort.
TOP            : sucht nach den 10 häufigsten Wörter, Ausgabe mit Anzahlen.
TEST           : Testmodus: gibt die gelesene Datei aus.
TEST number    : Testmodus: liest nur number Zeichen und gibt sie aus.
---> """)

mode, *args = user_input.split()

trump_speeches_path = Path(__file__).parent / "trump_speeches.txt"

with open(trump_speeches_path, mode="r", encoding="utf-8") as file:
    if mode == "TEST":
        if len(args) == 0:
            content = file.read()
        else:
            content = file.read(int(args[0]))
    else:
        content = file.read()  # Alles gelesen, nicht nur 5000 Zeichen.

content = content.replace("\n"," ")

if mode == "SEN":
    search_word = args[0]
    filtered_sentences = []
    all_sentences = content.split(".")
    for sentence in all_sentences:
        if search_word in sentence:
            filtered_sentences.append(sentence)
    print(filtered_sentences)
 
elif mode == "WORD" or mode == "TOP":
    # cleanup content: replace "--" by " "
    content = content.replace("--"," ").replace("\n"," ")
    all_words = content.split()
    clean_words = []
    for word in all_words:
        clean_word = word.replace(",","").replace(".","").replace("?","").replace(";","")
        if clean_word:
            clean_words.append(clean_word)
    if mode == "WORD":
        search_word = args[0]
        filtered_words_set = set()
        for word in clean_words:
            if search_word in word:
                filtered_words_set.add(word)
        print(list(filtered_words_set))
    if mode == "TOP":
        long_words_dict = {}
        for word in clean_words:
            word_lower = word.lower()
            if len(word_lower) >= 5:
                long_words_dict[word_lower] = long_words_dict.get(word_lower, 0) + 1
        # Cokeler: Mit Lambda wird sortiert
        # Das ging früher (Verson 2.*) einfacher, mit compare-Funktion, ohne Lambdas.
        sorted_items = sorted(long_words_dict.items(), key=lambda x: -x[1])
        print(sorted_items[:10])
elif mode == "TEST":
    print(content)



