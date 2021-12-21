# -*- coding: utf-8 -*-

import os

os.chdir('/home/benbel/adventofcode2021/06')

with open("input", "r") as fichier:
    ligne = fichier.readlines().pop()
    
poissons = [int(x) for x in ligne.split(',')]

iterate = lambda x: (x - 1) % 7 if x <= 7 else x - 1 

for jour in range(80):
    poissons = [iterate(x) for x in poissons] + len([_ for _ in poissons if _ == 0]) * [8]
    
print(len(poissons))