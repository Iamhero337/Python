a = input('Give the input: ')

i = 0
j = ''
while i<len(a):
    if 'a'<=a[i]<='z':
        j +=a[i]
    i+=1
print(j)

