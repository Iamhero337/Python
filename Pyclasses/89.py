a = lambda x:print(x[::-1]) if type(x) in [list,set,tuple,dict,str] else print(x)
a(eval(input("Give the input: ")))