num = int(input("Give the number: "))

value = 1
for i in range(4):   #Column
    for j in range(num):   #Row
        print(f"{value:3}", end=" ")
        value += 1
    print()
