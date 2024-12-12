num = int(input("Give the number to evaluate: "))

value = 0
for i in range(1, num+1):
    value += 1 / i

print(f"{value:.2f}")
