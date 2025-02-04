a = input("Give input: ")

if a == a[::-1]:
    print(a)
elif len(a)%2==0:
    print(a[::-1])
else:
    print(a[1::2])
