def gen(l):
    for i in l:
        # if type(i) == float:
        if isinstance(i,float):
            yield i
print(list(gen([10,10.25,20,20.25,30,30.25,40,40.25])))
        