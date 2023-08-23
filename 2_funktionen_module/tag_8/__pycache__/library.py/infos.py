""" 
Modul Infos

Stellt Funktionen zur Informationen über die Platform bzw. computer bereit
(via platform module)

"""
# Diese Funktionen werden geladen bei Star-Import
__all__ = ["computers_name", "opertaing_system"]
import platform


def computers_name():
    """get name of computer."""
    return platform.node()

def operating_system():
    return platform.platform()
