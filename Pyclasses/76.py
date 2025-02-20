#76. WAP to create 4 different function to perform addtion, substraction, mulliplication and division.

def add(a, b):
    return a+b
def minus(a, b):
    return a-b
def prod(a, b):
    return a*b
def div(a, b):
    return a/b

x, y = int(input("Give the first value: ")),int(input("Give the second value: "))

print(add(x, y))
print(minus(x, y))
print(prod(x, y))
print(div(x, y))


