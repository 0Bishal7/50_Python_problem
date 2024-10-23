# 23.Write a function that checks if a given year is a leap year.
def leap_year(year):
    if ( year % 4==0 and year % 100 != 0 ) or year % 400 == 0 :
        return True
    return False

print(leap_year(2023))



