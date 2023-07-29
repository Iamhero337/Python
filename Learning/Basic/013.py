uin = input("Give the string to check: ")
vow = 0
els = "aeiou"

for inps in uin:
     if inps in els:
         vow += 1

if vow == 0:
    print("There is no vowel in this sentence.")
elif vow == 1:
    print("There is 1 vowel in this sentence.")
else:
    print(f"There are {vow} vowels in this sentence.")
