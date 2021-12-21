# -*- coding: utf-8 -*-

import numpy as np
import os


def check_tableau(tableau, drawn_numbers):
    ligne_validee = min([len([nombre for nombre in ligne if not nombre in drawn_numbers]) for ligne in tableau]) == 0
    colonne_validee = min([len([nombre for nombre in colonne if not nombre in drawn_numbers]) for colonne in np.array(tableau).T]) == 0
    return (ligne_validee or colonne_validee)
                           

os.chdir('/home/benbel/adventofcode2021/04')

with open("input", "r") as fichier:
    lignes = fichier.readlines()


drawn_numbers = [int(x) for x in lignes.pop(0).removesuffix("\n").split(',')]

lignes = [[int(z) for z in x.removesuffix("\n").split(' ') if z] for x in lignes if x != '\n']

tableaux = [lignes[x:x+5] for x in range(0, len(lignes), 5)]

for i in range(len(drawn_numbers)):
    drawn_numbers_so_far = drawn_numbers[0:i]
    
    tableaux_valides = [check_tableau(tableau, drawn_numbers_so_far) for tableau in tableaux]
    if True in tableaux_valides:
        tableau_valide = tableaux[tableaux_valides.index(True)]
        break
        
unmarked_numbers = [nombre for ligne in tableau_valide for nombre in ligne if nombre not in drawn_numbers_so_far]

result = sum(unmarked_numbers) * drawn_numbers_so_far[-1]
print(result)
