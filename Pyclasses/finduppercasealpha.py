def numberofupperinstring():
    s = input("Give the input: ")
    count = 0
    for i in s:
        if 'A'<=i<='Z':
            count+=1
    print(count)


numberofupperinstring()
