print("String " + 4e-2) #MAL
print("String " + str(4e-2)) #BIEN

import funciones as mf # MAL
print(radtodeg(2.3))

import funciones as mf #BIEN
print(mf.radtodeg(2.3))

self.propelipticas.e # MAL
self.propelipticas['e'] # BIEN
