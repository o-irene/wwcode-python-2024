# Task: Create a program that checks if a year is a leap year.

def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


assert is_leap_year(2024) is True
assert is_leap_year(1700) is False
assert is_leap_year(2000) is True
assert is_leap_year(2021) is False
assert is_leap_year(2028) is True
