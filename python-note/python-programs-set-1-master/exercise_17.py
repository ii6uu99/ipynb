print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-17:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Task: b = a - 17;
#Conditions: 
# a > 17 => b = 2(a - 17);
# a <= 17 => b = a - 17;
#First solution:
'''
print("Calculation the difference between a given number and 17:")
a = int(input("Please enter the number = "))
if (a > 17):
  b = 2 * (a - 17)
  print("%d > 17, then = %d" % (a, b))
else:
  b = a - 17
  print("%d <= 17, then = %d" % (a, b))
'''
#Second appropriate solution:
def diff(n):
  if n <= 17:
    b = 17 - n
    print("%d <= 17, then = %d" % (n, b))
  else:
    b = (n - 17) * 2
    print("%d > 17, then = %d" % (n, b))

diff(int(input("Please, enter the number = ")))
diff(int(input("Please, enter the number = ")))

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )