from cmath import sqrt

def quadr_ecu(a, b, c):
    q = sqrt((b**2) - (4 * a * c))
    x1 = (-b + q) / 2*a
    x2 = (-b - q) / 2*a 
    return x1, x2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
result = quadr_ecu(a, b, c)
print(result)
print(f"x1: {result[0]:.3f}, {result[1]:.3f}")