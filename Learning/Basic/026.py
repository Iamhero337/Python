num = int(input("Give the value to print: "))
val = 0

for row in range(num):
    print("  " * row, val)
    val += 1
