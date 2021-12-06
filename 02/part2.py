# -*- coding: utf-8 -*-

import os

os.chdir('/home/benbel/adventofcode2021/02')

with open("input", "r") as fichier:
    donnees = [
        x.removesuffix("\n").split(' ')
        for x
        in fichier.readlines()
        ]

aim = 0
depth = 0
horizontal = 0

for x in donnees:
    instruction, value = x
    value = int(value)
    if instruction == "up":
        aim -= value
    elif instruction == "down":
        aim += value
    elif instruction == "forward":
        horizontal += value
        depth += aim * value

    else:
        print("Erreur")
        break

    
print(depth * horizontal)