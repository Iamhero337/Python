# name = input("Enter your name: ")
#
# while name == "":
#     print("You didn't put your name.")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}.")

num = int(input("Give a number between 1 to 12: "))

while num <= 1 or num >= 12:
    print(f"{num} is not valid")
    num = int(input("Give a number between 1 to 12: "))

print(f"Your choice of box, is {num}.")

