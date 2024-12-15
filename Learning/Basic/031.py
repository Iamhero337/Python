import sys

num = int(input("Give the value to determine: "))
result = 0

if num <= 0:
    print("No 0 or negative value is accepted.")
    sys.exit()
elif num <= 2:
    print(1)
    sys.exit()

a, b = 0, 1

for i in range(num):
    print(a, end=" ")  # Print the current Fibonacci number
    a, b = b, a + b
