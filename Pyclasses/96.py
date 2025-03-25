# #96. WAP to get fact number b/w range 1 to 100 store the output in the form of tuple.

# def fact(n):
#     t = 1
#     for i in range(1, n):
#         t *= i
#     return t
    

# def factcol(n):
#     for i in range(1, n+1):
#         yield fact(i)



# print(tuple(factcol(int(input("Give the collection to get factorial: ")))))

##2nd try to do something else
# n = int(input("Give the number to get factorial: "))


def fact(i=1,f=1,n):
    while i>n:
        return 
    fact(i+1,f*i,n)
fact(5)