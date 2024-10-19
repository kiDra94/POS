#!/usr/bin/env python
"""
.. modleauthor:: Drazen Plavsic <drazen.plavsic@example.com>
"""
user_f = float(input("Enter a temperature in degrees Fahrenheit: "))
celsius = 5/9*(user_f - 32)
print(f"{user_f} degrees Fahrenheit correspond to {celsius:.2f} degrees Celsius")