#!/usr/bin/env python
"""
.. moduleauthor:: Drazen Plavsic <drazen.plavsic@example.com>
"""

user = input("For C => F enter C, for F => C enter F: ")
if user == 'C':
   celsius = -20
   while celsius < 41:
       fahrenheit = 9/5 * celsius + 32
       print(f"{celsius} C => {fahrenheit:.2f} F")
       celsius += 1
elif user == 'F':
    fahrenheit = -10
    while fahrenheit < 111:
       celsius = 5/9*(fahrenheit - 32)
       print(f"{fahrenheit} F => {celsius:.2f} C")
       fahrenheit +=1