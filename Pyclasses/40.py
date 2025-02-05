a = input("Give the input: ")

ab = ''

i = 3
while i<len(a):
    if 'A'<=a[i]<='Z' and ord(a[i])%2 ==0:
        ab += a[i]
    i+=3
print(ab)
