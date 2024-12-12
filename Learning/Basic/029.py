num = int(input("Give the number to evaluate: "))

val = 0
for i in range(1, num+1):
    val += 1 / (i**2)

print(f"{val:.2f}")