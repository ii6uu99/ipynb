print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-18:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to test whether a number is within 100 of 1000 or 2000."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

def near_thousand(n):
  return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(near_thousand(534))
print(near_thousand(956))
print(near_thousand(1101))
print(near_thousand(1899))
print(near_thousand(2003))


print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )