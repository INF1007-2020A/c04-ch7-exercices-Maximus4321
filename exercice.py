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

def tree():
  setheading(90)
  color('green')
  speed(0)
  branch()

def branch(length=70, pen=7, angle=35):
  if length > 0 and pen > 0:
    pensize(pen)
    forward(length)
    right(angle)
    branch(length-10, pen-1, angle-5)
    left(angle*2)
    branch(length-10, pen-1, angle-5)
    right(angle)
    backward(length)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    tree()