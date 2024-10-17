year = int(input("Give the year: "))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("This a leap year.")
else:
    print("Not a leap year.")