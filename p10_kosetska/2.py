import numpy as np

years = np.arange(1900, 2020+3, 1)

while True:
    year = (input("Enter the year from 1900 to 2022:"))
    month = (input("Enter the month from 1 to 12:"))
    if len(list(year)) == 4 and len(list(month)) == 1 or len(list(month)) == 2 and int(year) >= 1900 and int(year) <= 2022 and int(month) >= 1 and int(month) <= 12:
        try:
            year = int(year)
            month = int(month)
            break
        except:
            print("Try again!")

def leap_years(i):
    return i % 400 == 0
intercalary = list(filter(leap_years, years))
print('leap year(s):', intercalary)

def not_leap_years(i):
    return i % 100 == 0
not_intercalary = list(filter(not_leap_years, years))
print('not a leap year(s):', not_intercalary)

def leap_years2(i):
    return i % 4 == 0
intercalary2 = list(filter(leap_years2, years))
print('a leap year(s):',intercalary2)

days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11]
days_28_or_29 = [2]

def days_monthes(years, func, year, month):
    leap_years = func(years)
    if month in days_31:
        print("Month number:", month, "in", year, "has 31 days")
    elif month in days_30:
        print("Month number:", month, "in", year, "has 30 days")
    elif year in leap_years and month in days_28_or_29:
        print("Month number:", month, "in", year, "has 29 days")
    elif month in days_28_or_29:
        print("Month number:", month, "in", year, "has 28 days")

days_monthes(years, leap_years2, year, month)