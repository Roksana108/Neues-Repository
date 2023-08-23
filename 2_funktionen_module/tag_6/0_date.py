""" 
Datum und Zeit in Python
datetime - Modul, alles was mit Datum zu tun hat
time - Modul: alles, was mit Zeit zu tun hat
"""
import time
import locale
from datetime import datetime, timedelta
from pytz import timezone

locale.setlocale(locale.LC_TIME, "de_DE")

# TIME
# Unix Timestamp: Sekunden seit 1.1.1970 (the Epoch)
print(f"unix timestamp: {time.time()}")
print(f"Unix timestamp in nanosekunden: {time.time_ns()}")
print(f"Zeitzone: {time.tzname}")  # CET 'Mitteleuropäische Zeit'
# print("1 Sekunde schlafen:", time.sleep(1))

# Datumsangaben (internationales Datumsformat)
# Format ist ISO 8601 (https://de.wikipedia.org/wiki/ISO_8601)
date_obj = datetime.now()  # aktueller Zeitpunkt (ohne Zeitzone)
print(f"jetzt: {date_obj}", type(date_obj))

some_date = datetime(year=2042, month=11, day=2)
print(f"Datum weit in der Zukunft: {some_date}")

utc = timezone("UTC")
christmas_2024 = datetime(year=2024, month=12, day=24, tzinfo=utc) # timezone aware!

# Datumsobjekte formatieren
# deutsches Datumsformat 24.12.2024
# https://www.programiz.com/python-programming/datetime/strftime
print("Weihnachten 2024 ist an einem:", christmas_2024.strftime("%A"))
print("Jahr Weihnachten 2024:", christmas_2024.strftime("%d.%m.%Y %H:%M:%S"))
print("Aktueller Zeitpunkt", date_obj.strftime("%d.%m.%Y %H:%M:%S"))
print("Monat von Weihnachten:", christmas_2024.strftime("%B"))
print("Zeitzone", christmas_2024.strftime("%Z"))  # Zeitzone UTC

date_obj_utc = datetime.now(tz=utc)  # aktueller Zeitpunkt (ohne Zeitzone)
print(f"{date_obj_utc:%d.%m.%Y %H:%M:%S}")  # via fstring-Datumsformat

""" 
help(time.strftime)
Commonly used format codes:

    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

"""