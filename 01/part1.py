# -*- coding: utf-8 -*-

import os

os.chdir('/home/benbel/adventofcode2021/01')

with open("input", "r") as fichier:
    donnees = [
        int(x.removesuffix("\n"))
        for x
        in fichier.readlines()
        ]

result = sum([
    donnees[i] > donnees[i - 1]
    for i in range(1, len(donnees))
    ])

print(result)

