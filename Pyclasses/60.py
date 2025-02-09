n = int(input("Give the value to check weather it's spy number or not: "))


sumofn = 0
productofn = 1

n2 = n
while n2 > 0:
    r= n2 % 10
    sumofn += r
    productofn *= r
    n2 //= 10

if sumofn == productofn:
    print("It's a spy number.")
else:
    print("It's is not a spy number.")

