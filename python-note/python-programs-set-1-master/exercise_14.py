print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-14:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to calculate number of days between two dates.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

from datetime import date
print('First date :')
date_year_1 = int(input("Year :"))
date_month_1 = int(input("Month : "))
date_day_1 = int(input("Day : "))
print("You entered the first date : %d-%d-%d" % (date_day_1, date_month_1, date_year_1))
print('-----------------------')
print('Second date :')
date_year_2 = int(input("Year : "))
date_month_2 = int(input("Month : "))
date_day_2 = int(input("Day : "))
print("You entered the second date : %d-%d-%d" % (date_day_2, date_month_2, date_year_2))
f_date = date(date_year_1, date_month_1, date_day_1)
l_date = date(date_year_2, date_month_2, date_day_2)
delta = l_date - f_date
print('-----------------------')
print("Number of days between dates = %d" % delta.days)

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )