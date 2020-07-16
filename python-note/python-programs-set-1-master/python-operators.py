print(
  '-----------------------------------------\n'\
  'Practical python education || Python Operators:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Explore and analyze all available types of operators on the Python.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Default variables:
comparison_counter = 0

#Default function for handling execution loop:
def execution_loop():
  data = input("Do you want to try again ? Enter [1] - for continue / [0] - for quit : ")
  if data == 1:
    return True
  elif data == 0:
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
    execution_loop()

#Function for testing all available arithmetic operators on the Python:
def arithmetic_func(x, y):
    print('\nArithmetic operations\n')
    print('{0} + {1} = {2}'.format(x, y, x+y))
    #print(f'{x} - {y} = {x-y}')
    print('{0} - {1} = {2}'.format(x, y, x-y))
    if (y == 0):
      #print(f'You cannot divide {x} by zero.')
      print('You cannot divide {0} by zerp.'.format(x))
    else:
      #print(f'{x} / {y} = {x/y}')
      #print(f'{x} // {y} = {x//y}')
      print('{0} / {1} = {2}'.format(x, y, x/y))
      print('{0} // {1} = {2}'.format(x, y, x//y))
    #print(f'{x} * {y} = {x*y}')
    #print(f'{x} ^ {y} = {x**y}')
    print('{0} * {1} = {2}'.format(x, y, x*y))
    print('{0} ** {1} = {2}'.format(x, y, x**y))

#Function for testing all available comparison operators on the Python:
def comparison_func(x, y):
  print('\nComparison operations for operands:\n')
  comparator = x > y
  command = 'greater_than'
  print(comparison_string_func(command, comparator, x, y, 1))
  comparator = x < y
  command = 'less_than'
  print(comparison_string_func(command, comparator, x, y, 2))
  comparator = x == y
  command = 'equal_to'
  print(comparison_string_func(command, comparator, x, y, 3))
  comparator = x != y
  command = 'not_equal_to'
  command = 'not_equal_to'
  print(comparison_string_func(command, comparator, x, y, 4))
  comparator = x >= y
  command = 'greater_equal'
  print(comparison_string_func(command, comparator, x, y, 5))
  comparator = x <= y
  command = 'less_equal'
  print(comparison_string_func(command, comparator, x, y, 6))

#Function for testing logical operators on the Python:
def logical_func():
  print('\nLogical operations for operands:')
  x = boolean_input(1)
  print('You entered operand: {0}'.format(x))
  y = boolean_input(2)
  print('You entered operand: {0}\n'.format(y))
  comparator = x and y
  command = 'and'
  print(logical_string_func(command, comparator, 1))
  comparator = x or y
  command = 'or'
  print(logical_string_func(command, comparator, 2))
  comparator = not x
  command = 'not'
  print(logical_string_func(command, comparator, 3))
  comparator = not y
  command = 'not'
  print(logical_string_func(command, comparator, 4))

#Function for bitwise operators on the Python:
def bitwise_func():
  print('\nBitwise operations for operands:\n')
  print('Please, enter your 1-operand integer')
  x = int(input('>>> '))
  print('Please, enter your 2-operant integer')
  y = int(input('>>> '))
  print('Your entered integers on the 8-bit binary representation:')
  print('{0}: {0:08b}'.format(x, x))
  print('{0}: {0:08b}'.format(y, y))
  print('\nResults of bitwise operations:\n')
  print('{0} AND {1} = {2} : {2:08b}'.format(x, y, x & y, ))
  print('{0} OR {1} = {2} : {2:08b}'.format(x, y, x | y))
  print('{0} XOR {1} = {2} : {2:08b}'.format(x, y, x ^ y))
  print('{0} NOT = {1} : {1:08b}'.format(x, ~x))
  print('{0} NOT = {1} : {1:08b}'.format(y, ~y))
  print('{0} >> 3 = {1} : {1:08b}'.format(x, x >> 3))
  print('{0} >> 2 = {1} : {1:08b}'.format(y, y >> 2))
  print('{0} << 6 = {1} : {1:08b}'.format(x, x << 6))
  print('{0} << 3 = {1} : {1:08b}'.format(y, y << 3))

#Function for assignment operators on the Python:
def assignment_func():
  print('\nAssigment operations for operands:\n')
  print('Please, enter your 1-operand integer')
  x = int(input('>>> '))
  print('Please, enter your 2-operand integer')
  y = int(input('>>> '))
  print('{0} = {0} + {1} = {2}'.format(x, y, x += y))
  print('{0} = {0} - {1} = {2}'.format(x, y, x -= y))
  print('{0} = {0} * {1} = {2}'.format(x, y, x *= y))


def boolean_input(index):
  print('\nPlease, enter your {0}-operand with only values: True [1] / False [0]:'.format(index))
  user_input = int(input('>>> '))
  if user_input == 1:
    return True
  elif user_input == 0:
    return False
  else:
    print('Error: "{0}" entered operand is not equal to "1" or "0"... Please try again...'.format(user_input))
    return boolean_input(index)

def logical_string_func(operation, comparator, index):
  message = {
    'and': 'Two operands are True' if comparator else 'One operand is not True',
    'or': 'One or two operands are True' if comparator else 'All operands are not True',
    'not': 'Operand is True' if comparator else 'Operand is False'
  }[operation]
  output = '{0}. {1}'.format(index, message)
  return output
  

def comparison_string_func(operation, comparator, x, y, index):
  message = {
    'greater_than': 'is greater than' if comparator else 'is not greater than',
    'less_than': 'is less than' if comparator else 'is not less than',
    'equal_to': 'is equal to' if comparator else 'is not equal to',
    'not_equal_to': 'is not equal to' if comparator else 'is equal to',
    'greater_equal': 'is greater or equal to' if comparator else 'is not greater or equal to',
    'less_equal': 'is less or equal to' if comparator else 'is not less or equal to'
  }[operation]
  #output = f'{index}. Operand {x} {message} {y}.'
  output = '{0}. Operand {1} {2} {3}'.format(index, x, message, y)
  return output

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  print("Please, enter your operands for starting all necessary operations:")
  x = float(input('x = '))
  y = float(input('y = '))
  arithmetic_func(x, y)
  comparison_func(x, y)
  logical_func()
  bitwise_func()
  assignemnt_func()
  counter_exec = counter_exec + 1
  again_exec = execution_loop()

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )