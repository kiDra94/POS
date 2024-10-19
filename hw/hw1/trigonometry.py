from math import sin, tan, pi
print("radians | sine | tangent\n---------------------")

i = 0.0
PI = pi

while i < pi:
    print(f"{i:>7.1f} | {round(sin(i), 2):>5} | {round(tan(i), 2):7}")
    i+=0.1
print(f"{pi:>7.2f} | {round(sin(pi), 2):>5} | {round(tan(pi), 2):>7}")
