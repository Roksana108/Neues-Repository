""" 
Der else Zweig: Wird immer ausgeführt, wenn KEINE Exception aufgetreten ist.
"""
import sys

d = {
    "a": 3
}

try:
    d["a"]  # d["b"] Key Error!
    hugo = "ootto"
    y = 3 / 0
except KeyError as e:
    print("Hier ist ein Key-error aufgetreten!")
    print(e)
except ZeroDivisionError as e:
    y = float("inf")
except:
    print(sys.exc_info())   # in Log Datei schreiben
else:
    print("Es ist kein Fehler aufgetreten!")
finally:
    print("hugo", hugo)

print(f"{y=}")