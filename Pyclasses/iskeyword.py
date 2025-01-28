import keyword
    

a = input("Give the strign to check is it a keyword?: ")

if keyword.iskeyword(a):
    print("This is a keyword.")
else:
    print("Not a key word")
