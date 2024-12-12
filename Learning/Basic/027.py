num = int(input("Give the value to print: "))

for row in range(1, num + 1):
    for spaces in range(num - row):
        print(" ", end="")
    for stars in range(row):
        print("* ", end="")
    print()
