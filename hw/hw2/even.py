#!/usr/bin/env python
"""
.. moduleauthor:: Drazen Plavsic <drazen.plavsic@example.com>
"""

upper_limit = int(input("Upper limit: "))

for i in range(0, upper_limit, 2):
    i = i**2
    if i <= upper_limit:
        print(i)