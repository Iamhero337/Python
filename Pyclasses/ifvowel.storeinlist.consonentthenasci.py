a = input("Give the input: ")

l = []

if a in 'aeiouAEIOU':
    l.append(a)
    print(l)
else:
    print(ord(a))
