# Imports
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

PI = np.arccos(-1)

# Funciones Útiles
def radtodeg(angle):
    deg = angle * (180 / PI)
    return deg

def degtorad(angle):
    rad = angle * ( PI / 180)
    return rad

def ejeperpendicular(vector):
    modulo = np.sqrt(vector.dot(vector))
    x = vector[0]
    y = vector[1]
    eje = np.array([y/modulo, -x/modulo])
    return eje

def secstohours(time):
    h = time/3600
    return h
