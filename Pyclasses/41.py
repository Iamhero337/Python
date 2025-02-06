#41. WAP to find the sum of all ascii value of all sp.char present inside the given string.

a= input("Give the input: ")

sum=0
i=0

while i<len(a):
    if not ('a'<=a[i]<='z' or 'A'<=a[i]<='Z' or '0'<=a[i]<='9'):
        sum += ord(a[i])
    i+=1
print(sum)
