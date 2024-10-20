uname = input("Give the username: ")

length = len(uname)

if length > 12 :
    raise Exception("You did not follow the guidelines.")

if " " in uname or any(char.isdigit() for char in uname):
    print("You did not follow the guidelines.")
else:
    print(uname + " is assigned.")