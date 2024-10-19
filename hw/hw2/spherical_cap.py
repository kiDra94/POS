#!/usr/bin/env python
"""
.. moduleauthor:: Drazen Plavsic <drazen.plavsic@example.com>
"""

from math import pi

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

surface = 2*radius*height*pi
volume = ((pi * (height)**2) / 3) * (3 * radius - height)

print(f"The spherical cap has a surface of {surface:.3f}")
print(f"The volume of the spherical cap is {volume:.3f}")