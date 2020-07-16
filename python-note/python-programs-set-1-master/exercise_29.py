print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-29:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.\n'
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

#Function for handling input colors:
def color_inputs_handling(index):
  print("Please, enter your ", index, "-st color_list:")
  col_loop_param = True
  color_counter = 0
  c_list = []
  start_par = True
  while col_loop_param:
    if start_par:  
      color_counter = color_counter + 1
      print("Color-%d:" % color_counter)
      c_list.append(input(""))
    par = input("Do you want to add a new color to the color_list_1 ? Enter [y] - for adding a new color / [n] - for launching input a new color_list_2 :")
    if par == "y":
      col_loop_param = True
      start_par = True
    elif par == "n":
      col_loop_param = False
    else:
      col_loop_param = True
      start_par = False
      print("Error: you entered incorrect command. Please, try again...")

  return set(c_list)

#Default parameters for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  color_list_1 = color_inputs_handling(1)
  color_list_2 = color_inputs_handling(2)
  print("You entered color_list_1 wihout color_list_2 elements:")
  print(color_list_1.difference(color_list_2))
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