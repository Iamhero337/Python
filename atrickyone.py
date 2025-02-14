# s = input("Give the input: ")
# dic={}
# c = 0
#
# for i in s.split():
#     dic[i] = len(i)
# print(dic)

s = input("Give the input: ")
dic={}


for i in s.split():
    c = 0
    for j in i:
        if j in 'AEIOUaeiou':
            c+=1
        dic[i]= [i[::-1], c, i[::2]]

print(dic)
