""" 
Vorkommnisse von Zeichen in einem String zählen

{
    "a": 4,
    "b": 1,
    "t": 3,
}
"""
sentence = "the brown fox \njumps over the lazy \nfox"
words = {}

# WORD COUNTER
for word in sentence.split():
    word = word.strip()
    if word in words:
        words[word] += 1   # a = a + 1 => a += 1
    else:
        words[word] = 1

print(words)

# CHAR COUNTER
d = {}
for char in sentence:
    value = d.get(char, 0) + 1
    d.update({char:value})

print(d)


a = 3
a /= 2  # a = a / 2
