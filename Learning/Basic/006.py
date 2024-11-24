name = input("Name: ")
roll = int(input("Roll: "))
class_ = input("Class: ")
eng = float(input("Marks in English: "))
mat = float(input("Marks in Math: "))
phy = float(input("Marks in Physics: "))
bio = float(input("Marks in Bio: "))

grade = (eng + mat + phy + bio) / 4

# Define the width of the box
box_width = 50

print("+" + "-" * (box_width - 2) + "+")

# Format each line dynamically
print(f"| Roll:        {roll:<{box_width - 13}}|")
print(f"| Name:        {name:<{box_width - 13}}|")
print(f"| Class:       {class_:<{box_width - 13}}|")
print(f"| Percentage:  {grade:.2f}%{' ' * (box_width - 17 - len(f'{grade:.2f}'))}|")

print("| Grade:       ", end="")
if grade >= 80:
    print(f"A{' ' * (box_width - 18)}|")
elif grade >= 60:
    print(f"B{' ' * (box_width - 18)}|")
elif grade >= 50:
    print(f"C{' ' * (box_width - 18)}|")
elif grade >= 45:
    print(f"D{' ' * (box_width - 18)}|")
else:
    print(f"F{' ' * (box_width - 18)}|")

print("+" + "-" * (box_width - 2) + "+")
