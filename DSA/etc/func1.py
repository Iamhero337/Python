def sumofn(n):
   total = 0
   for i in range(1,n+1):
       total += i
   return total

n = int(input("Give the number: "))

if n < 0:
    print("Give a positive number.")

else:
    result = sumofn(n)
    print("The sum of natural number up to", n, "is:", result)