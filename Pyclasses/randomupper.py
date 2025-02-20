#73. WAP to find uppercase alphabets present inside the given string.


def countupper(a):
    count = 0
    for i in s:
        if 'A'<=i<='Z':
            count+=1
    return count

s = input("Give the input: ")
print(countupper(s))
