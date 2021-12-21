# -*- coding: utf-8 -*-

from collections import Counter

import os


def generate_intermediate_line_points(ligne):
    a, b = ligne
    x_a, y_a = a
    x_b, y_b = b
    
    points = {
        (x, y)
        for x in range(min(x_a, x_b), max(x_a, x_b) + 1)
        for y in range(min(y_a, y_b), max(y_a, y_b) + 1)
        }
    
    
    return points
    
    
os.chdir('/home/benbel/adventofcode2021/05')

with open("input", "r") as fichier:
    lignes = [
        [tuple(int(k) for k in point.split(',')) for point in x.removesuffix("\n").split(' -> ')]
        for x in fichier.readlines()
        ]


non_diagonal_lines = [
    ligne for ligne in lignes
    if (ligne[0][0] == ligne[1][0]) or (ligne[0][1] == ligne[1][1])
    ]

nested_points = [generate_intermediate_line_points(ligne) for ligne in non_diagonal_lines]
points = [point for ligne in nested_points for point in ligne]

multi_line_points = [key for key, value in Counter(points).items() if value >= 2]
print(len(multi_line_points))