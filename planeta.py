# Imports
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import funciones as mf

# Constantes
G = 6.67408e-11 # N m^2 kg^-2

# Clase Planeta
class Planeta:
    """CLASE Q DEFINE LOS PLANETAS"""

    def __init__(self, datos, M):
        self.nombre = datos['nombre']
        self.masa = datos['masa']
        self.radio = datos['radio']
        self.propelipticas = {
            "e": datos['excentricidad'],
            "a": datos['semiejemayor'],
            "b": datos['semiejemayor'] * np.sqrt(1 - (datos['excentricidad'])**2),
            "c": datos['excentricidad'] * datos['semiejemayor']
        }
        self.M = M

        # Asignamos las posiciones, velocidades y aceleraciones iniciales
        self.r = np.array([self.propelipticas['a'] - self.propelipticas['c'], 0.])
        self.v = np.array([0.,-1 * np.sqrt(2 * G * self.M * ((1 / np.sqrt(self.r.dot(self.r))) - (1 / (2 * self.propelipticas['a']))))])

        amod = (G * self.M)/(self.r.dot(self.r))
        self.theta = np.arctan2(self.r[1], self.r[0])
        #print(mf.radtodeg(theta))
        self.a = np.array([-1 * amod * np.cos(self.theta), -1 * amod * np.sin(self.theta)])

        self.h = np.sqrt(G * self.M * self.propelipticas['a'] * (1 - (self.propelipticas['e'])**2))

    def drawOrbit(self, linspace, ejes):
        x = self.propelipticas['a'] * np.cos(np.radians(linspace)) - self.propelipticas['c']
        y = self.propelipticas['b'] * np.sin(np.radians(linspace))

        ejes.plot(x, y, color='grey')

    def listEverything(self):
        print(self.nombre.upper())
        print("Masa = " + str(self.masa))
        print("Radio = " + str(self.radio))
        print("Propiedades Elípticas = " + str(self.propelipticas))
        print("Posición = " + str(self.r))
        print("Velocidad = " + str(self.v))
        print("Aceleración = " + str(self.a))
        print("\n")

    def listRVA(self):
        print(self.nombre.upper())
        print("Posición = " + str(self.r))
        print("Velocidad = " + str(self.v))
        print("Aceleración = " + str(self.a))
        print(mf.radtodeg(self.theta))
        print("")

    def update_deprecated(self, dt):
        self.r = self.r + self.v * dt
        self.v = self.v + self.a * dt

        amod = (G * self.M)/(self.r.dot(self.r))
        self.theta = np.arctan2(self.r[1], self.r[0])
        self.a = np.array([-1 * amod * np.cos(self.theta), -1 * amod * np.sin(self.theta)])

    def update(self, dt):
        self.r = self.r + self.v * dt
        self.theta = np.arctan2(self.r[1], self.r[0])

        vmod = np.sqrt(2 * G * self.M * ((1 / np.sqrt(self.r.dot(self.r))) - (1 / (2 * self.propelipticas['a']))))
        #direccion = mf.ejeperpendicular(self.r)
        lodedentro = self.h/(np.linalg.norm(self.r) * vmod)
        #phi = np.arcsin(lodedentro)

        if lodedentro > 1:
            phi = np.arccos(-1)/2
        else:
            phi = np.arcsin(lodedentro)
        direccion = np.array([np.cos(self.theta + phi), np.sin(self.theta + phi)])
        self.v = direccion * vmod

        amod = (G * self.M)/(self.r.dot(self.r))
        self.a = np.array([-1 * amod * np.cos(self.theta), -1 * amod * np.sin(self.theta)])

    def returnR(self):
        return [self.r[0], self.r[1]]

    def returnX(self):
        return self.r[0]

    def returnY(self):
        return self.r[1]

    def outputR(self):
        file = open('output.txt', 'a')
        file.write(str(self.r[0]) + " " + str(self.r[1]) + "\n")
        file.close()

    def outputRv2(self):
        file1 = open('outputx.txt', 'a')
        file2 = open('outputy.txt', 'a')

        file1.write(str(self.r[0]) + "\n")
        file2.write(str(self.r[1]) + "\n")

        file1.close()
        file2.close()

    def outputRVA(self):
        file = open('output.txt', 'a')

        file.write(self.nombre.upper() + "\n")
        file.write("Posicion = " + str(self.r) + "\n")
        file.write("Anomalia Verdadera = " + str(mf.radtodeg(self.theta)) + "\n")
        file.write("Velocidad = " + str(self.v) + "\n")
        file.write("Aceleracion = " + str(self.a) + "\n")
        file.write("\n")

        file.close()

    def fancyOutput(self):
        file = open('output.md', 'a')

        file.write("## " + self.nombre.upper() + "\n")
        file.write("``` \n")
        file.write("Posicion = " + str(self.r) + "\n")
        file.write("Anomalia Verdadera = " + str(mf.radtodeg(self.theta)) + "\n")
        file.write("Velocidad = " + str(self.v) + "\n")
        file.write("Aceleracion = " + str(self.a) + "\n")
        file.write("``` \n")

        file.close()
