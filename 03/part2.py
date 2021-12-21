# -*- coding: utf-8 -*-

import copy
import numpy as np
import os


def pseudo_binary_to_decimal(binary_list):
    reverse_list = binary_list[::-1]
    decimal_list = [x * 2**indice for indice, x in enumerate(reverse_list)]
    return sum(decimal_list)


def find_digit(donnees, pattern):
    data = copy.deepcopy(donnees)
    for digit_position in range(len(data[0])):
        
        value = [pattern(x) for x in np.array(data).sum(axis = 0) >= len(data)/2.0][digit_position] 
        data = [number for number in data if number[digit_position] == value]
        if len(data) == 1:
            break
        
    return data[0]


os.chdir('/home/benbel/adventofcode2021/03')

with open("input", "r") as fichier:
    donnees = [
        [int(z) for z in x.removesuffix("\n")]
        for x
        in fichier.readlines()
        ]

donnees = np.array(donnees)

binary_oxygen = find_digit(donnees, lambda x: int(x))
oxygen = pseudo_binary_to_decimal(binary_oxygen)

binary_co2 = find_digit(donnees, lambda x: 1 - int(x))
co2 = pseudo_binary_to_decimal(binary_co2)

print(oxygen * co2)
