t = eval(input("Give the value: "))

if type(t)==tuple:
    if len(t)%2!=0:
        mid=len(t)//2
        if type(t[mid])==str:
            if len(t[mid])>3:
                print(t[mid])
            else:
                print("It is not more than 3 in length.")
        else:
            print("It is not string.")
    else:
        print("The tuple doesn't have middle value as it is not odd in lenght.")
else:
    print("It is not a tuple.")
