num = int(input("Give the value to draw: "))

for row in range(1, num + 1):
    # for spaces in range(num - row):
    #     print(" ", end="")
    # for stars in range(2*row-1):
    #     print("*", end="")
    # print()

    #Made the whole damn code interesting
    print(" " * (num - row) + "*" *(2 * row - 1))

