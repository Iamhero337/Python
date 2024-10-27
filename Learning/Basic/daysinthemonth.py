def num_days(month):
    months = {
        "jan": 31,
        "feb": 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31
    }
    print(months[month])

    # if month == 'jan':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'apr':
    #     print('number of days in',month,'is',30)
    # elif month == 'may':
    #     print('number of days in',month,'is',31)
    # elif month == 'jun':
    #     print('number of days in',month,'is',30)
    # elif month == 'jul':
    #     print('number of days in',month,'is',31)
    # elif month == 'aug':
    #     print('number of days in',month,'is',31)
    # elif month == 'sep':
    #     print('number of days in',month,'is',30)
    # elif month == 'oct':
    #     print('number of days in',month,'is',31)
    # elif month == 'nov':
    #     print('number of days in',month,'is',30)
    # elif month == 'dec':
    #     print('number of days in',month,'is',31)


name_of_the_month = input("Give the month to get the dates in it: ")
num_days(name_of_the_month)
# optimize/shorten the code in the function
# try to reduce the number of conditionals
