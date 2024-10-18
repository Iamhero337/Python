#Python calculator

operator = input("Enter a operator(* / - +): ")

num1 = float(input("Enter the 1st operand: "))
num2 = float(input("Enter the 2nd operand: "))

result = None

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("You have given wrong operator as option.")

if result is not None:
    print(result)