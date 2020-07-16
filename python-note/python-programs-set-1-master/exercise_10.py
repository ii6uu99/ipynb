print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-10:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print("Result =", n1+n2+n3)

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )