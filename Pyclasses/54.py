#54. WAP to extract all the vowels present inside the given string.

s = input("Give the input: ")
a = ''
i = 0
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        a += s[i]
    i+=1
print(a)
