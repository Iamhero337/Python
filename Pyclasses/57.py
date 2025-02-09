n2 = int(input("Give the value to check weather it's a armstrong number or not: "))
n = n2
sumofn = 0
r = 0
while n > 0:
    r = n % 10
    sumofn += r**3
    n //= 10
if sumofn == n2:
    print("It's a armstrong number.")
else:
    print("It's not a armstrong number.")
