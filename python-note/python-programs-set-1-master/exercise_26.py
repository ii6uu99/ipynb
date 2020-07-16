print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-26:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to create a histogram from a given list of integers.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

#Default function for handling execution loop:
def execution_loop():
  data = input("Do you want to try again ? Enter [y] - for continue / [n] - for quit : ")
  if data == "y":
    return True
  elif data == "n":
    return False
  else:
    print("Error: your entered incorrect command. Please, try again...")
    execution_loop()

#Function for building a new histogram based on user group data:
def histogram(items):
  print('Histogram was builded based on your array data:')
  for n in items:
    output = ''
    times = n
    while (times > 0):
      output += '*'
      times = times - 1
    print(output, ' ', n)

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  user_arr_length = int(input("Please, enter length of your array = "));
  print("Please, enter array elements:")
  user_arr = []
  for i in range(user_arr_length):
    print("%d-th: " % i)
    user_arr.append(int(input("")))
  print("You entered array: ", user_arr)
  histogram(user_arr)
  again_exec = execution_loop()
  counter_exec = counter_exec + 1

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ",counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )