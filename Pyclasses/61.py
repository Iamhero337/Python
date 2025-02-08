#61. Perfect number or not.( the sum of the factor should be equal to the number.)

n = int(input("Give the int to check perfect or not: "))

sumofn=0
i=1
while i<n:
    if n % i ==0:
        sumofn +=i
    i+=1
if n == sumofn:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")