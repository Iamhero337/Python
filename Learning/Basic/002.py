name = input("Name: ")
age = int(input("Age(int): "))
salary = int(input("Salary(int): "))

print("Name:        ",name)
print("Age:         ",age)
print("Salary:      ",salary)
print("Designation:  ", end="")

if salary < 10001:
    print("Unknown")


elif 10000 < salary <= 20000:
    print("Intern")

elif salary <= 35000:
    print("Jr. SDE")

else:
    print("Product Manager")

