# Imports
import json
from planeta import *
from sistema_planetario import *
import numpy as np
import matplotlib.pyplot as plt
import funciones as mf
import time


# Testeos
#test_import()

# Programa Principal
with open("input.json") as input_file:
    JSON = json.load(input_file)

planetatest = Planeta(JSON['planetas'][2], JSON['estrella']['masa'])

while True:
    planetatest.listRVA()
    #planetatest.outputR()
    #planetatest.outputRv2()
    planetatest.outputRVA()
    planetatest.update(1e0)


    time.sleep(1e-3)
