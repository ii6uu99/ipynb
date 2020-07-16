print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-28:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.\n'
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

#Function for printing all numbers of the entered data list, before identified 237:
def print_data_list(n):
  user_data_list = []
  even_numbers = 0
  for x in range(n):
    print("%d-th: " % x)
    new_element = int(input(""))
    user_data_list.append(new_element)

  print("Your data list: ", user_data_list)
  for x in user_data_list:
    if x == 237:
      print("237 was identified! Here printing function is complete.")
      break
    elif x % 2 == 0:
      even_numbers = even_numbers + 1
      print("%d is an even number" % x)
  print("In your data list are =", even_numbers," even numbers")

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  user_list_length = int(input("Please, enter length of your list data = "))
  if user_list_length == 0:
    print("Error: you entered a 0. List data can't be empty. Please, try again...")
    continue
  elif user_list_length < 0:
    print("Error: you entered a negative number. Length of data list can't be negative number. Please, try again...")
    continue
  else:
    print_data_list(user_list_length)
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