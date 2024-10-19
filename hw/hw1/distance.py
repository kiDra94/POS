from math import sqrt

f_x = float(input("first x: "))
f_y = float(input("first y: "))
s_x = float(input("scnd x: "))
s_y = float(input("scnd y: "))

e_d = sqrt((s_x - f_x)**2 + (s_y - f_y)**2)

print(f"The euclidean distance between the two points is {e_d:.4f}")