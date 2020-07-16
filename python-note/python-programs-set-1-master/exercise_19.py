print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-19:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is " + str

print(new_string(input("Enter your string: ")))
print(new_string(input("Enter your string again: ")))


print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )