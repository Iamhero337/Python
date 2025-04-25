# #ZerDiv Error handling
#
#
#
# try:
#     n1=int(input('Give the value of n1: '))
#     n2=int(input('Give the value of n2: '))
#     print(n1/n2)
# except ZeroDivisionError:
#     print('Zero division Error.')
#     n2=int(input('Re-enter the value of n2: '))
#     print((n1/n2))




#Zero div handling with loop
# n1 = int(input('Give the value of n1: '))
# i=0
# while True:
#
#     try:
#
#         n2=int(input('Give the value of n2: '))
#         print(n1/n2)
#         break
#     except ZeroDivisionError:
#         print('Zero division Error.')
#     i+=1


#Value Error
#
# try:
#     s=int(input('Give a number: '))
#     print(s)
# except ValueError:
#     s=int(input("You didn't give a number, Give the value again: "))
#     print(s)


# #Type Error
# s2=12
# try:
#     s = input("Give the 1st String: ")
#     print(s+s2)
# except TypeError:
#     s2 = input("Again Give the 2nd part of string: ")
#     print(s + s2)



#Handling multiple exception in one single except block


try:
    n1=int(input('Give the 1st number: '))
    n2=int(input('Give the 2nd value: '))
    s='Iamhero337'
    res = n1+n2
    print(res)
    print(s[res])

except (ValueError, TypeError, IndexError,NameError) as e:
    if type(e)==ValueError:
        print('ValueError is handled.')
        n1=int(input('re-enter n1:'))
        n2=int(input('re-enter n2: '))
        s = 'Iamhero337'
        res = n1 + n2
        print(res)
        print(s[res])

    elif type(e)==TypeError:
        print('TypeError is handled.')
        n1 = int(input('re-enter n1:'))
        n2 = int(input('re-enter n2: '))
        s = 'Iamhero337'
        res = n1 + n2
        print(res)
        print(s[res])

    elif type(e)==IndexError:
        print('IndexError is handled.')
        print('The sum of n1 and n2 is more than the size of the string. lower the values accordingly.')
        n1 = int(input('re-enter n1:'))
        n2 = int(input('re-enter n2: '))
        s = 'Iamhero337'
        res = n1 + n2
        print(res)
        print(s[res])
