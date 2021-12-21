# -*- coding: utf-8 -*-

import numpy as np
import os

os.chdir('/home/benbel/adventofcode2021/03')

with open("input", "r") as fichier:
    donnees = [
        [int(z) for z in x.removesuffix("\n")]
        for x
        in fichier.readlines()
        ]

donnees = np.array(donnees)
lignes, colonnes = donnees.shape

gamma_binary = [int(x) for x in donnees.sum(axis = 0) > lignes/2.0] 
epsilon_binary = [1 - x for x in gamma_binary]

def pseudo_binary_to_decimal(binary_list):
    reverse_list = binary_list[::-1]
    decimal_list = [x * 2**indice for indice, x in enumerate(reverse_list)]
    return sum(decimal_list)

gamma = pseudo_binary_to_decimal(gamma_binary)
epsilon = pseudo_binary_to_decimal(epsilon_binary)

print(gamma * epsilon)