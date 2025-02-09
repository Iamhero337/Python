#56. WAPT take homogeneous intiger list, divide the input collection into 2 diffrent list. output the first list it should consist of even numbers and the second list which should be only consisting of odd numbers.

n = eval(input("Give a homogeneous intiger list: "))

i = 0
while i<len(n):
    if not type(n[i]) == int:
        print("You have not given a homogeneous initger list.")
        exit()
    i+=1

evenl = []
oddl = []

i = 0
while i<len(n):
        if n[i] % 2 == 0:
            evenl.append(n[i])
        else:
            oddl.append(n[i])
        i+=1

print(n)
print(evenl)
print(oddl)
