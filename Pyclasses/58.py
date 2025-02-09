# WAPT map two different list in a from of dictionary.
l1 = ['anda','thanda','jhanda',123, 2+5j, 222]
l2 = ['danda','garam','fanda',321,69+5j, 666]

fl = {}
if len(l1) == len(l2):
    i = 0
    while i<len(l2):
        fl[l1[i]] =l2[i]
        i+=1
print(fl)
