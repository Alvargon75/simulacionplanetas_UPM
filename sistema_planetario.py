# Imports
import json
from planeta import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import funciones as mf

# Clase Sistema Planetario
class SistemaPlanetario:
    """
    CLASE Q DEFINE EL SISTEMA PLANETARIO, CONTIENE LOS PLANETAS
    """

    def __init__(self, JSON):
        self.t = 0
        self.ticks = 0
        self.nombre = JSON['nombre']

        self.estrella = {
            "nombre": JSON['estrella']['nombre'],
            "masa": JSON['estrella']['masa'],
            "radio": JSON['estrella']['radio']
        }

        self.planetas = []

        for pln in JSON['planetas']:
            temppln = Planeta(pln, self.estrella['masa'])
            self.planetas.append(temppln)

    def listEverything(self):
        for pln in self.planetas:
            pln.listEverything()

    def listRVA(self):
        print("t = " + str(mf.secstohours(self.t)))
        for pln in self.planetas:
            pln.listRVA()

    def drawOrbits(self, ejes):
        espacio = np.linspace(0, 360, 360)

        for pln in self.planetas:
            pln.drawOrbit(espacio, ejes)

    def update(self, dt=1e+2):
        self.t += dt
        self.ticks += 1

        for pln in self.planetas:
            pln.update(dt)

    def returnR(self):
        coordinates = []
        for pln in self.planetas:
            coordinates.append(pln.returnR())

        return coordinates

    def returnX(self):
        Xes = []
        for pln in self.planetas:
            Xes.append(pln.returnX())

        return Xes

    def returnY(self):
        Yes = []
        for pln in self.planetas:
            Yes.append(pln.returnY())

        return Yes

    def getName(self):
        return self.nombre

    def output(self):
        file = open('output.txt', 'a')
        file.write("t = " + str(mf.secstohours(self.t)) + "\n")
        file.close()

        for pln in self.planetas:
            pln.outputRVA()

        file = open('output.txt', 'a')

        file.write("--------------------------------------------------------------------------------------------------------------------- \n")

        file.close()

    def fancyOutput(self):
        file = open('output.md', 'a')
        file.write("# t= " + str(mf.secstohours(self.t)) + " h \n")
        file.close()

        for pln in self.planetas:
            pln.fancyOutput()

        file = open('output.md', 'a')
        file.write("*** \n")
        file.close()
