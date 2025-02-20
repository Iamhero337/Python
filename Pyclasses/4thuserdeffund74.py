#74. WAP to extract integer numbers present at odd indexes only if they are divisible by 5 from a list.

n = eval(input("Give the input: "))

en = ''
for i in range(len(n)):
    if i%2 != 0 and n[i]%5 == 0:
        en+=str(n[i])
        en+=' '
print(en)
