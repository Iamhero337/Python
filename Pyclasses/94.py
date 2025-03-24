def lm(ldata):
    for i in ldata:
        if isinstance(i,int):
            yield i,len(str(i))
            
print(list(lm([5.6,789,1111,2+5j,'Priya'])))
    