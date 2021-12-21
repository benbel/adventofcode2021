# -*- coding: utf-8 -*-

from collections import Counter

import os


def generate_intermediate_straight_line_points(ligne):
    a, b = ligne
    x_a, y_a = a
    x_b, y_b = b
    
    points = {
        (x, y)
        for x in range(min(x_a, x_b), max(x_a, x_b) + 1)
        for y in range(min(y_a, y_b), max(y_a, y_b) + 1)
        }
    
    
    return points
    


def generate_intermediate_diagonal_line_points(ligne):
    a, b = ligne
    x_a, y_a = a
    x_b, y_b = b
    
    left_point = a if x_a <= x_b else b
    right_point = b if x_a <= x_b else a
    
    x_l, y_l = left_point
    x_r, y_r = right_point
    
    increment = 1 if y_r > y_l else -1 # positive slope if right point is above left point
    
    points = [
        (x_l + i, y_l + i * increment)
        for i in range(x_r - x_l + 1)
        ]
    
    
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

diagonal_lines = [
    ligne for ligne in lignes
    if ligne not in non_diagonal_lines
    ]

nested_points_straight = [generate_intermediate_straight_line_points(ligne) for ligne in non_diagonal_lines]
nested_points_diagonal = [generate_intermediate_diagonal_line_points(ligne) for ligne in diagonal_lines]
nested_points = nested_points_diagonal + nested_points_straight

points = [point for ligne in nested_points for point in ligne]

multi_line_points = [key for key, value in Counter(points).items() if value >= 2]
print(len(multi_line_points))