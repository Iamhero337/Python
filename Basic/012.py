user_input = input("Enter a string: ")
caret_string = ""

for char in user_input:
    if char.isdigit():
        caret_string += "^"
    else:
        caret_string += " "

print(user_input)
print(caret_string)
