print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-27:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to concatenate all elements in a list into a string and return it.\n'
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

#Function for concatenating all list elements and returns a string from them:
def concatenating_list_data(list):
  result = ''
  for element in list:
    result += str(element)
  print(result)

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  user_list_length = int(input("Please, enter length of your list = "))
  if user_list_length < 0:
    print("Error: Lenght of the list cannot be a negative number. Please, try again...")
    continue
  elif user_list_length == 0:
    print("Error: The list must have at least one item. Please, try again...")
    continue
  else:
    user_list = []
    output = ''
    for i in range(user_list_length):
      print("%dth: " % i)
      user_list.append(input())
    print("Your entered list data: ", user_list)
  concatenating_list_data(user_list)
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