balls = [
    "grün"
    "rot"
    "blau"
]

#  counts: die Anzahl der Elemente pro Eleemnt der Population 
# Zufällig k Bälle aus der Populatin mit 3000 Bällen ziehen 
random_balls = random.sample(balls, counts=[1000, 1000, 1000], k=100)
print(random_balls)