principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Give the principle amount: "))
    if principle <= 0:
        print("The principle can't be 0 or less than it.")
while rate <= 0:
    rate = float(input("Give the interest rate: "))
    if rate <= 0:
        print("The rate can't be 0 or less than it.")
while time <= 0:
    time = float(input("Give the number of periods in year: "))
    if time <= 0:
        print("The time can't be less than 1 year.")

famt = principle*(1 + rate/100)** time

print(f"The amount will be ${famt:.2f} after {time} year/s with the rate of interest {rate}%. ")