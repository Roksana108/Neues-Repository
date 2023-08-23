"""
CSV-Dataien einlsen 
CSV-Dialekte: semikolon, Komma, tab

Schema:
value1, value2, value3
12,2,3,4
"hamburg", "berlin, tiergarden","dresden", "leipzig" 

"""


from pathlib import Path

with open(Path(__file__).parent / "data.csv") as f:
    for line in f:
        #  values = [float(num) for num in line.split(",")]
        values = line.split(", ")
        print(values)