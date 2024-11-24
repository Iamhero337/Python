a = float(input("Give the first side(a): "))
b = float(input("Give the first side(b): "))
c = float(input("Give the first side(c): "))

if a == b == c:
    print("This triangle is Equilateral.")

elif a == b or a == c or b == c :
    print("This triangle is a Isosceles.")
else:
    print("This triangle is a Scalene.")