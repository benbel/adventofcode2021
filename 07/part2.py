# -*- coding: utf-8 -*-

import numpy as np
import os

os.chdir('/home/benbel/adventofcode2021/07')

with open("input", "r") as fichier:
    ligne = fichier.readlines().pop()
    
coordonnees = np.array([int(x) for x in ligne.split(',')])

def compute_cost(coordonnees, position):
    distances = np.absolute(coordonnees - position)
    fuel_cost = ((distances * (distances + 1))/ 2).sum()
    return fuel_cost

mean = round(np.mean(coordonnees))
candidates = [mean - 1, mean]

fuel_cost_by_position = {
    position:  compute_cost(coordonnees, position)
    for position in candidates
    }

min_cost = min([cost for position, cost in fuel_cost_by_position.items()])

optimum = {
    (position, cost)
    for position, cost
    in fuel_cost_by_position.items()
    if cost == min_cost
    }

print(optimum)