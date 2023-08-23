"""
Built in Scope: Vorsicht vor dem Überschreiben von built-in Functions
"""
id = 23
x = 3


def _print():
    print("das geht auch nicht")


def fn():
    def _print():
        print("inner")
    print("Im lokalen Scope")
    # print(y) NameError, da y in keinem Scope gefunden wird
 

fn()
print("im globalen Scope")