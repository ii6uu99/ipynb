print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-7:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to accept a filename from the user and print the extension of that.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

filename = input("Input the filename: ")
f_extns = filename.split(".")
print('The extension of the file is: ' + repr(f_extns[-1]))

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )