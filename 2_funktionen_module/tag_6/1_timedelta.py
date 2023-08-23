""" 
Timedelta: Rechnen mit Datumsangaben
"""
from datetime import datetime, timedelta

heute = datetime.today()
birthday = datetime(year=1990, month=11, day=1)

# --------------------------------------------------------------
# Zwei Daten voneinander abziehen
# --------------------------------------------------------------
alter = heute - birthday  # Timedelta - Objekt
print(type(alter), alter.days)
print("Sekunden seit Geburt:", alter.seconds * 60 * 60 * 24)

# --------------------------------------------------------------
# Tage abziehen oder dazurechnen
# --------------------------------------------------------------
heute = datetime.today()
zwei_tage_in_zukunft = heute + timedelta(days=2)
print(f"heute:", heute)
print(f"zwei tage in zukunft:", zwei_tage_in_zukunft)

# --------------------------------------------------------------
# Sekunden/Stunden abziehen oder dazurechnen
# --------------------------------------------------------------
zwei_stunden_in_zukunft = heute + timedelta(hours=2)
print(zwei_stunden_in_zukunft)
