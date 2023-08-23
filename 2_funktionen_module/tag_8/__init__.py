"""
wird immer ausgeführt, wenn package importiert wird
__init__.py ist notwendig für:

- Package-Dokumentation
- Dunder Variablen
- Pre-Imports
- Funktionen defieren, Datenbankzugriff etablieren,
- Logger konfigurieren

https://peps.python.org/pep-0008/#module-level-dunder-names
"""
__author__ = "B.F <hi@example.com>"
__version__ = "0.5.1"
__copyright__ = "Copyright 2023"
__credits__ = ["WBS"]
__license__ = "GPL"
__maintainer__ = "Sponge Bob"
__email__ = "hi@example.com"
__status__ = "Production"


from .infos import *
