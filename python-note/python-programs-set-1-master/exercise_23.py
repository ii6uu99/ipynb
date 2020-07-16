print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-23:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

str = input("Enter your string = ")
n = abs(int(input("Enter amount for clonning of the string = ")))

#First solution:
'''
res = ""
output = ""
if len(str) < 2:
  res = str;
else:
  res = str[:2]

for i in range(n):
  output = output + res

print("Clonning copies from your string:")
print(output)
'''

#Second solution:
def substring_copy(str, n):
  result = ""
  flen = 2
  if flen > len(str):
    flen = len(str)
  substr = str[:flen]
  for i in range(n):
    result = result + substr
  return result

print("Clonning copies from your string:")
print(substring_copy(str, n))


print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )