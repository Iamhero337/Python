#53. to extract all the svd present inside the given list.

lis = eval(input("Give the list: "))
elis = []
i = 0
while i<len(lis):
    if type(lis[i]) in (int, bool, complex, float):#if type(lis[i])== (int or bool or complex or float): (what the heck is wrong with this #error)
        elis.append(lis[i])
    i+=1
print(elis)
