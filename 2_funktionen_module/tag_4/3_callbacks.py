"""
Callbacks

A callback is a funktion that is passed as a argument to another funtion 
This other funtion is extected to call this callback funktion 
"""


import time

def printer(element):
    print("Printer druck aus:", element)


def costly_fn(seconds, callback):
    """Arbeitet eine zeitlang und ruft dannach eine Function auf."""
    time.sleep(seconds)
    result = [1, 2, 3, 4]
    callback(result)
  
  
costly_fn(2, printer)

