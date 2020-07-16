print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-15:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to get the the volume of a sphere with radius 6."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

from math import pi
r = 6.0
d = r*2
V1 = 4.0/3.0 * pi * r**3
V2 = pi * (d**3 / 6.0)
print('Volume of a sphere with radius 6(m) = ', V1, '(m^3)')
print('Volume of a sphere with diameter 12(m) = ', V2, '(m^3)')

print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )