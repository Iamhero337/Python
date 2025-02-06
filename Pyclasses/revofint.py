n = int(input("Give the input: "))

rev = 0
r = 0

while n>0:
    r = n%10
    rev=(rev*10)+r
    n//=10
print(rev)

