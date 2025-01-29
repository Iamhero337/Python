a = input("Give the input: ")

if a.isupper() or a.islower():
    print(a*5)
elif not('a'<=take<='z' or 'A'<=take<='Z' or '0'<=take<='9'):
    b = ord(a)
    b +=5
    b = chr(b)
