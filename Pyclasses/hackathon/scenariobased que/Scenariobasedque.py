#ATM cash dispense
s = int(input("Give the amount to be dispensed: "))
uid = input("Enter the user id: ")

s2=s
atm_100=0
atm_500=0
atm_2000=0
atm_bal=200000
user_a=0
user_b=0
user_c=0


if s % 100 == 0:
    if s<=50000:
        if s<=atm_bal:
            if uid not in ["user_a","user_b","user_c"]:
                print("Invalid user")
                exit()
            else:
                if uid == "user_a":
                    if user_a+s<=100000:
                        user_a=user_a+s
                    else:
                        print("Daily limit exceeded")
                elif uid == "user_b":
                    if user_b+s<=100000:
                        user_b=user_b+s
                    else:
                        print("Daily limit exceeded")
                elif uid == "user_c":
                    if user_c+s<=100000:
                        user_c=user_c+s
                    else:
                        print("Daily limit exceeded")
            
                
            atm_bal=atm_bal-s
            print(f"Amount dispensed: {s}")
            # print(f"ATM balance: {atm_bal}")
            atm_2000=s2//2000
            s2-=2000*int(atm_2000)
            atm_500=s2//500
            s2-=500*int(atm_500)
            atm_100=s2//100
            s2-=100*int(atm_100)
            print(f"The notes you are going to get: {atm_2000}*2000 and {atm_500}*500 and {atm_100}*100 ", )
        else: 
            print("Insufficient balance")
    else:
        print("Maxium withdrawal limit exceeded")
else:
    print("Invalid amount")
   