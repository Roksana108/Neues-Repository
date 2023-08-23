""" 
Ein Datetime-Objekt aus einem String parsen für strptime
"""
from datetime import datetime

# -----------------------------------------------------------------
# Wenn das Datum im ISO-8601 Format gegeben ist, dann fromisoformat
# -----------------------------------------------------------------
t1 = "2019-12-24 18:00:00"
dateobj_from_iso = datetime.fromisoformat(t1)
print(dateobj_from_iso)

# -----------------------------------------------------------------
# unbekanntes Datumsformat mit strptime angeben
# -----------------------------------------------------------------
t2 = "2019 1 11"
dateobj_from = datetime.strptime(t2, "%Y %m %d")
print(dateobj_from.strftime("%d.%m.%Y"))
print(f"{dateobj_from:%d.%m.%Y}")