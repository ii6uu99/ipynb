print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-3:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to display the current date and time."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

import datetime;
now = datetime.datetime.now()
print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )