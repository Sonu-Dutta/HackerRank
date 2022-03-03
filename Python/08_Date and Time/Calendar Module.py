import calendar
MM, DD, YYYY = map(int,input().split())
print (calendar.day_name[calendar.weekday(YYYY,MM,DD)].upper())