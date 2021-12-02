# -*- coding: utf-8 -*-

import os

os.chdir('/home/benbel/adventofcode2021/01')

with open("input", "r") as fichier:
    donnees = [
        int(x.removesuffix("\n"))
        for x
        in fichier.readlines()
        ]

sommes = [
    sum(donnees[i-1:i+2])
    for i in range(1, len(donnees) - 1)
    ]

result = sum([
    sommes[i] > sommes[i - 1]
    for i in range(1, len(sommes))
    ])

print(result)

