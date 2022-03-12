# 1 Jan 1900 was a Monday.

# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap_year(year):
    if year % 4 == 0 and not year % 400 == 0:
        return True
    return False

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def first_of_next_month(days, day_delta):
    return (days % 7 + day_delta) % 7

# print(first_of_next_month(31, 1))
# 5219
day_delta = 2
sundays = 0
for year in range(1901, 2000):
    for i in days_in_month:
        if is_leap_year(year) and i == 28:
            i = 29
            day_delta = first_of_next_month(i, day_delta)
        else:
            day_delta = first_of_next_month(i, day_delta)

        if day_delta < 3 and i >= 30:
            sundays += 5
        elif 3 <= day_delta <= 6 or i == 28:
            sundays += 4
        elif i == 29:
            if day_delta == 0:
                sundays += 5
            else:
                sundays += 4
        else:
            print("wtf")

print(sundays)
# def counting_sundays(start, end, day_of_week):
#     for year in range(start[2], end[2]):
