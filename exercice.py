#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
import sys
sys.path.insert(1,r"C:\Users\Maxime\Documents\GitHub\c04-ch6-exercices-Maximus4321")
from exercice2 import frequence

import turtle
# TODO: Définissez vos fonction ici

def compute_volume_mass(a=2,b=4,c=2,p=10):
    volume=(4/3)*math.pi**a*b*c
    mass=p*volume
    return mass,volume




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass