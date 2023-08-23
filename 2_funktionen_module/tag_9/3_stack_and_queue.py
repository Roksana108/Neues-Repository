"""
Stack (Stapel, LIFO) und Queue (Warteschlange, FIFO),
zwei wichtige Datensturkturen
"""

from collections import deque  # double linked list

# ------------------------------------------------------------------------------
# Stack (LAST IN, FIRST OUT), zwei wihtige Methoden: push und pop
# ------------------------------------------------------------------------------
stack = []
stack.append(2)
stack.append(4)
stack.append(5)

print("Der aktuelle Stack:\n", stack)
print("das letzte item: ", stack.pop())
print("Der aktuelle Stack:\n", stack)

# ------------------------------------------------------------------------------
# Warteschlage, Queue (FIRST IN, FIRST OUT), zwei Methoden: enqueue und dequeue
# ------------------------------------------------------------------------------
queue = []
queue.append(2)
queue.append(4)
print("Die aktuelle Warteschlange:\n", queue)
print("das erste item: ", queue.pop(0))
print("Die aktuelle Warteschlange:\n", queue)

# ------------------------------------------------------------------------------
# für schnelle Implementierung von Stack und insebsondere Queue den Datentyp deque
# verwenden (doubly linked list)
# ------------------------------------------------------------------------------
dec = deque(["a", "b", "c"])
print(dec)

# append
dec.append("d")
print(dec)

# left append
dec.appendleft("first")
print(dec)

# pop
dec.pop()
print(dec)

# popleft
dec.popleft()
print(dec)

# maximaleinträge der Deque
browserhistory = deque(["amazon.com", "google.de", "ebay.de"], maxlen=3)
print(browserhistory)
browserhistory.appendleft("twitter.com")
print(browserhistory)

browserhistory.rotate(2)
print(browserhistory)


dec2: deque[str] = deque()
apples: list[int] = []