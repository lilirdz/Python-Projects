import math


# check for leap year
def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True


# check if date is within the gregorian calendar
def is_gregorian_date(year, month, date):
    if (year == 1752) and (month == 9) and (date == 14):
        return True
    if (year == 1752) and (month == 9) and (date > 14):
        return True
    if (year == 1752) and (month > 9):
        return True
    if (year > 1752):
        return True
    else:
        return False


# check if date is valid in terms of month, date, and leap year
def is_valid_date(year, month, date):
    if (is_gregorian_date(year, month, date) == False):
        return False
    if (month > 12) or (date > 31):
        return False
    if (year == 1752) and (month == 9) and (date == 14):
        return True
    if (month == 4) and (1 <= date <= 30):
        return True
    if (month == 6) and (1 <= date <= 30):
        return True
    if (month == 9) and (1 <= date <= 30):
        return True
    if (month == 11) and (1 <= date <= 30):
        return True
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)\
            and (1 <= date <= 31):
        return True
    if (is_leap_year(year) == True) and (month == 2) and (1 <= date <= 29):
        return True
    if (is_leap_year(year) == False) and (month == 2) and (1 <= date <= 28):
        return True
    else:
        return False


# use Zeller's formula to calculate weekday
def weekday_of(year, month, date):
    if 0 < month < 3:
        month += 12
        year -= 1
    # M is month 3 = March ...  14 = Feb
    M = month
    # C is zero based century (year/100)
    C = int(year / 100)
    # Y is the year of the century (year % 100)
    Y = int(year % 100)
    # D is day of the month
    D = date
    # day_num is day of the week 0= Saturday 1= Sunday... 6 = Friday
    day_num = (D + (math.floor((13 * (M + 1)) / 5)) + Y + (math.floor(Y / 4)) + (math.floor(C / 4)) + (5 * C))
    day_num = day_num % 7
    return day_num


# find what day of the week weekday_of function corresponds to
def weekday_name(weekday):
    if weekday == 0:
        return 'Saturday'
    if weekday == 1:
        return 'Sunday'
    if weekday == 2:
        return 'Monday'
    if weekday == 3:
        return 'Tuesday'
    if weekday == 4:
        return 'Wednesday'
    if weekday == 5:
        return 'Thursday'
    if weekday == 6:
        return 'Friday'
    else:
        return False


# input birthday to see what day of the week you were born
def main():
    birthday = input('Enter your birthday in YYYY-MM-DD format:\n')
    birthday = birthday.split('-')[0:3]
    birthday = [int(n) for n in birthday]
    year = birthday[0]
    month = birthday[1]
    date = birthday[2]
    greg_date = is_gregorian_date(year, month, date)
    valid_date = is_valid_date(year, month, date)
    birthday = weekday_of(year, month, date)
    weekday = weekday_name(birthday)

    if (greg_date == True) and (valid_date == True):
        print('You were born on a', weekday + '!')

    else:
        print('The date you entered is invalid.')


if __name__ == '__main__':
    main()
