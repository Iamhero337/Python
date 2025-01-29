a = input("Give the char: ")

if 'A'<=a<='Z':
    b = ord(a)+32
    print(chr(b))
else:
    print("It is not a upper case char.")
