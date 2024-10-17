import math


p = float(input("Give the perpendicular of the triangle: "))
b = float(input("Give the base of the triangle: "))

hypotenuse = math.sqrt(pow(p, 2)+pow(b, 2))

print(f"The hypotenuse is: {hypotenuse}")