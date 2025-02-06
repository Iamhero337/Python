#49. WAP to count the number of occurance of a specified character in a given string.

n = input("Give the input: ")
val = input("Give the char to get to know the repetation of it in the earlier sentence: ")

i = 0
num=0
while i<len(n):
    if val == n[i]:
        num+=1
    i+=1
print(num)
