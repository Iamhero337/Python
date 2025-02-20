#78.  reverse a string and keep the words as it is( I love you, you love I).


s = input("Give the input: ")

def reversestringbutnotword(a):
    s = ''
    ls = a.split()
    num = len(ls)
    while num > 0:
        num-=1
        s= ' '.join(ls[num])
        # s+=ls[num]

    return str(s)

print(reversestringbutnotword(s))


