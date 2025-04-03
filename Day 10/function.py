# def format_name(f_name, l_name):
#     return f_name.title() + " " +l_name.title()
#
# full_name = format_name(f_name="jame",l_name="bond")
# print(full_name)

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    return month_days[month -1]

year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
days = days_in_month(year, month)
print(f"There are {days} days in month {month} of year {year}")