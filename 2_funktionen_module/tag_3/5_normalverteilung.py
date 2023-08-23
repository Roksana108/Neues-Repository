"""
Zufälliger Wert aus einer (Standard)-Normalverteilung
"""
import random
import matplotlib.pyplot as plt

random.seed(42)

mu = 0
sigma = 1

print(f"Zufälliger Wert aus Standard Normalverteilung: {random.gauss(mu, sigma)}")
numbers = [random.gauss(mu, sigma) for _ in range(1_000)]


plt.hist(numbers, bins=50)
plt.title("Histogramm der Standard Normalverteilung")
plt.show()

# random.normalvariate wäre eine Alternative