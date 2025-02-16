s = input("Give the input: ")
c = input("Give the char to check: ")
num = -1
for i in s:
    num+=1
    if i == c:
        break
print(num)
