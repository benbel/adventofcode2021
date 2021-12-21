# -*- coding: utf-8 -*-

from collections import Counter

import os

os.chdir('/home/benbel/adventofcode2021/06')

with open("input", "r") as fichier:
    ligne = fichier.readlines().pop()
    
poissons = dict(Counter([int(x) for x in ligne.split(',')]))


for jour in range(256):
    nouveaux_poissons = dict()
    nombre_jeunes_poissons = poissons.get(0, 0)
    
    for age in [0, 1, 2, 3, 4 , 5 , 7]:
        nouveaux_poissons[age] = poissons.get(age + 1, 0)
        
    nouveaux_poissons[6] = nombre_jeunes_poissons + poissons.get(6 + 1, 0)
    nouveaux_poissons[8] = nombre_jeunes_poissons
    poissons = nouveaux_poissons
    
nombre_poissons = sum([value for key, value in poissons.items()])
print(nombre_poissons)
