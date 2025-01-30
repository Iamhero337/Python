a = input("Give val1: ")
b = input("Give val2: ")
c = input("Give val3: ")
d = input("Give val4: ")

if a>b:
    if a>c:
        if a>d:
            print(f'Val1 {a} is greatest.')
        else:
            print(f'Val4 {d} is greatest.')
    elif c>d:
        print(f'Val3 {c} is greatest.')
    else:
        print(f'Val4 {d} is greatest.')
elif b>c:
    if b>d:
        print(f'Val2 {b} is greatest.')
    else:
        print(f'Val4 {d} is greatest.')
elif c>d:
    print(f'Val3 {c} is greatest.')
else:
    print(f'Val4 {d} is greatest.')
