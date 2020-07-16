print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-6:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

values = input("Input some comma separated numbers : ")
list = values.split(',')
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )