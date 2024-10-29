import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def circumradius(a, b, c):
    S = calculate_area(a, b, c)
    return (a * b * c) / (4 * S)

def inradius(a, b, c):
    S = calculate_area(a, b, c)
    p = (a + b + c) / 2
    return S / p

a, b, c = 5, 6, 7
print("Радіус описаного кола:", circumradius(a, b, c))
print("Радіус вписаного кола:", inradius(a, b, c))
