#50. WAP to check weather the number is prime number or not.

n = int(input("Give the number to check prime or not: "))
i=2

while i<n:
    if n%i==0:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number")
    i+=1
