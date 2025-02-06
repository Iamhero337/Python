#48. WAP to check weather the given number is palindrome or not without using slicing or typecasting.

n = int(input("Give the input: "))

val1=n

lastn = 0
pal = 0
while n>0:
    lastn = n%10
    pal = (pal*10)+lastn
    n//=10
if pal == val1:
    print(f"{pal} is palindrome.")
else:
    print(f"{pal} is not a palindrome.")
