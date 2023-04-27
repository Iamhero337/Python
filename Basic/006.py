name = input("Name: ")
roll = int(input("Roll: "))
class_ = input("Class: ")
eng = float(input("Marks in English: "))
mat = float(input("Marks in Math: "))
phy = float(input("Marks in Physics: "))
bio = float(input("Marks in Bio: "))

grade = (eng+mat+phy+bio)/4

print("+------------------------------------------------+")

print(f"| Roll:         {roll}                               |")
print(f"| Name:         {name}                             |")
print(f"| Class:        {class_}                              |")
print("| Percentage:  ", grade, "%                           |")
print("| Grade:         ", end="")

if grade >= 80:
    print("A                               |")

elif grade >= 60:
    print("B                               |")

elif grade >= 50:
    print("C                               |")

elif    grade >= 45:
    print("D                               |")

else:
    print("F                               |")

print("+------------------------------------------------+")