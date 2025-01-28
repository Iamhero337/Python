s= eval(input())

if type(s) in [int, float, bool, complex]:
    print("Single value data-type")
else:
    print("Multiple value data-type")
