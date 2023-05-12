uin = input("Give the string: ")
caret = ""

for pri in uin:
    if pri.isdigit():
        caret += "^"
    else:
        caret += " "

print(uin)
print(caret)


