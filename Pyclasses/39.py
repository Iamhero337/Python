val = eval(input("Give the list data: "))

i = 0
b = []
while i<len(val):
    if type(val[i]) == str:
        if len(val[i])>3:
            b.append(val[i])
    i+=1
print(b)

