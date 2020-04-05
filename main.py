# Imports
import json
from planeta import *
from sistema_planetario import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import funciones as mf
import time

# Config
outputtxt = False
dt = 1e4
tickrate = 1e0
y_limit = (-0.1e13, 0.1e13)
x_limit = (-0.1e13, 0.1e13)

# Pa verlos todos
# y_limit = (-0.5e13, 0.5e13)
# x_limit = (-0.5e13, 0.5e13)

# Pa ver los pequeños (mercurio, venus, tierra, marte)
# y_limit = (-0.1e13, 0.1e13)
# x_limit = (-0.1e13, 0.1e13)

# Programa Principal

with open("input.json") as input_file:
    JSON = json.load(input_file)

sistema = SistemaPlanetario(JSON)

# Voy a testear el plotting
fig = plt.figure()
ejes = fig.add_subplot()

def main():
    while True:
        sistema.listRVA()
        sistema.fancyOutput()
        sistema.update(dt)
        time.sleep(tickrate)

def mainplot(i):
    x = sistema.returnX()
    y = sistema.returnY()

    if outputtxt:
        sistema.fancyOutput()

    sistema.update(dt)

    ejes.clear()
    ejes.plot(x, y, '.b')

    #sistema.drawOrbits(ejes)
    lins = np.linspace(0, 360, 360)

    for pln in sistema.planetas:
        x = pln.propelipticas['a'] * np.cos(np.radians(lins)) - pln.propelipticas['c']
        y = pln.propelipticas['b'] * np.sin(np.radians(lins))

        ejes.plot(x, y)



    sol=plt.Circle((0,0), radius=sistema.estrella['radio']*12.5, color='orange')
    plt.gcf().gca().add_artist(sol)

    plt.xlim(x_limit)
    plt.ylim(y_limit)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(sistema.getName() + " (t= " + str(round(mf.secstohours(sistema.t), 2)) + "h)")


#main()
ventana = anim.FuncAnimation(fig, mainplot, interval=tickrate)
plt.show()
