#77. WAPTE all the digits from the given string.
def getintfromstring(a):

    es = ''
    for i in s:
        if '0'<=i<='9':
            es+=i
    return es

s = input("Give the input: ")
print(getintfromstring(s))
