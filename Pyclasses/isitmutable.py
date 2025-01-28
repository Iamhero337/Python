data = eval(input("Give your data: "))


if type(data) in [list, set, dict]:
    print('Mutable')
else:
    print('Not mutable')
