#62. Fibonaaci...
val = int(input("Give the number to get the fibonacci of it: "))

x,y=0,1

if val < 0:
    print("Give a value greater than Zero.")
elif val == 1:
    print("The 1 Fibonacci number is 0.")
elif val == 2:
    print("The 2 Fibonacci number is 1.")      
else:
    print(x,end=' ')
    print(y,end=' ')
    
    i=3
    while i <= val:
       x, y = y, x + y
       print(y,end=' ')
       i+=1
print()