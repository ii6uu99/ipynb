print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-20:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to get a string which is n (non-negative integer) copies of a given string."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

def larger_string(str, n):
  result = ""
  for i in range(n):
    result = result + str
  return result

user_input = input("Enter string for n-clonning = ")
amount = abs(int(input("Enter amount of clonning for the string = ")))

print("Result")
print(larger_string(user_input, amount))

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )