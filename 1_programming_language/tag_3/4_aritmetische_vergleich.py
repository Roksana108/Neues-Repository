"""
Arithmetische Vergleichsoperatoren

== ist gleich
!= ist ungleich
> größer als
< kleiner als
>= größergleich als
<= kleinergleich als
!= ungleich

"""

alter_1 = 69
alter_2 = 69

name = "Paul"

print("Alter von Mensch 1 und Mensch 2: ", alter_1 == alter_2)

if (alter_1 == alter_2) and (name == "Paul"):
    print("die beiden Personenen sind gleich alt und name ist paul")

# 5 Minuten
geburtsort = input("Bitte Geburtsort eingeben: ")

if geburtsort == "Hamburg":
    print("ich bin in HH geboren")


# Person die älter als 69 bekommt einen Rentnerausweis
if alter_1 > 69:
    print("Person bekommt den Rentner Parkausweis")

# Person die jünger als 18 Jahre ist, darf nicht in den Club
if alter_2 < 18:
    print("Person darf nicht in den Club")

