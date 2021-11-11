import calendar


# print(calendar.TextCalendar(firstweekday=0).formatyear(2021))
# print(calendar.TextCalendar(firstweekday=0).formatmonth(themonth=9, theyear=2021))


month, day, year = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
