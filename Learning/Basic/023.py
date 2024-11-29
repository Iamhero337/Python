num = int(input("Give the value to print: "))

for row in range(0, num + 1):
    for star in range(num - row):
        print("*", end=" ")
    print()