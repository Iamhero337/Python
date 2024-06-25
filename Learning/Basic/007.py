choice = input("\033[Enter 'C' to convert from Fahrenheit to Celsius,"
               " or 'F' to convert from Celsius to Fahrenheit\n\n"
               "Choice (C/F): \033[0m")

if choice == 'C':
    fahrenheit = float(input("Give the Fahrenheit value: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"{fahrenheit} is equal to {celsius: .2f} °C.")

elif choice == 'F':
    celsius = float(input("Give the Celsius Value: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} is equal to {fahrenheit: .2f} °F.")

else:
    print("Invalid choice. Please enter 'C' or 'F'. ")
