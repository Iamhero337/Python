num = int(input("Give the number to evaluate: "))

val = 0
for i in range(1, num + 1):
    if i % 2 != 0:  # Odd position
        val += 2 * (i // 2) + 1
    else:  # Even position
        val += 2 * (i // 2)

print(val)
