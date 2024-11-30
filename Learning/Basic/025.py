num = int(input("Give the value to print: "))

for row in range(0, num + 1):
    for space in range(row):
        print(" ", end = " ")
    for star in range(1):
        print("*", end = " ")
    print()