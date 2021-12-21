# -*- coding: utf-8 -*-

import numpy as np
import os

os.chdir('/home/benbel/adventofcode2021/07')

with open("input", "r") as fichier:
    ligne = fichier.readlines().pop()
    
coordonnees = np.array([int(x) for x in ligne.split(',')])

optimal_position = np.median(coordonnees)
fuel_cost = np.absolute(coordonnees - optimal_position).sum()

print(fuel_cost)

