import csv
from pathlib import Path

with open(Path(__file__).parent / "worldcities.csv ") as f:
    reader = csv.reader(f, delimiter=",")
    print(reader)   
