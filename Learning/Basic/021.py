num = int(input("Give the number to print according to it: "))

val = 1

for i in range(1, num+1):
    for j in range(i):
        print(val, end=" ")
        val += 1
    print()