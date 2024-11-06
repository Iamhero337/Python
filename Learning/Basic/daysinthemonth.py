def num_days(month):
    if month in {"jan", "mar", "may", "jul", "aug", "oct", "dec"}:
        return 31
    elif month in {"apr", "jun", "sep", "nov"}:
        return 30
    elif month == "feb":
        return 28
    else:
        return "Invalid month"

name_of_the_month = input("Give the month (e.g., jan, feb): ").lower()
print(num_days(name_of_the_month))
