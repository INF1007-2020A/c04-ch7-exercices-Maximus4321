#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
import sys
import turtle
from turtle import *
# TODO: Définissez vos fonction ici

def compute_volume_mass(a=2,b=4,c=2,p=10):
    volume=(4/3)*math.pi**a*b*c
    mass=p*volume
    return mass,volume

def arbre(repetitions):
    color('green')
    pensize(10)
    left(90)
    forward(50)
    n=0
    while n<=repetitions:
        n+=1
        pensize(10-n)
        left(30)
        forward(12/(n+1))
arbre(50)
def tree(n):
  color('green')
  if n == 1:
    left(90)
    forward(15)
    left(30)
    forward(15)
    backward(15)
    right(60)
    forward(15)
    backward(15)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    arbre(50)
    tree(1)