def getstring(l,out=[],i=0):
    if i >= len(l):
        return out
    if type(l[i]) == str:
        out.append(l[i])
    return getstring(l,out,i+1)

print(getstring(eval(input("Give the list to get string: "))))
