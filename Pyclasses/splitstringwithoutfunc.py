s = input("Give the input: ")
out=['']

for i in s:
    if i == ' ':
        out+=' '
    else:
        out[-1]+=1
print(out)
