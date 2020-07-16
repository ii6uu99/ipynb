print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-12:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to print the calendar of a given month and year.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

import calendar
y = int(input("Input the year :"))
m = int(input("Input the month :"))
print(calendar.month(y, m))

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )