""" 
Modul: infos

Stellt Funktionen zur Informationen über die Platform bzw. computer bereit
(via platform module)

"""
# diese Funktionen werden geladen bei Star-Import
import platform

__all__ = ["computers_name", "operating_system", "cpu"]


def computers_name():
    """get name of computer."""
    return platform.node()

def operating_system():
    return platform.platform()

def cpu():
    return platform.processor()