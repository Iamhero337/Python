a = input("Give the input: ")

if 'a'<=a<='z' or 'A'<=a<='Z':
    print(a*5)
elif '0'<=a<='9':
    print(int(a)/5)
else:
    print(chr(ord(a)+5))
