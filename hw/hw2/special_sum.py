#!/usr/bin/env python
"""
.. moduleauthor:: Drazen Plavsic <drazen.plavsic@example.com>
"""

denominator = int(input("Denominator: "))
upper_limit = int(input("Upper limit: "))
sume_help = 0

for i in range(0, upper_limit+1, denominator):
     i += sume_help
     sume_help = i

print(f"Sum: {i}")