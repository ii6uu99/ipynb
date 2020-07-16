print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-25:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to check whether a specified value is contained in a group of values.\n'
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

#Function for checking out membership of the group data:
def is_group_member(group_data, n):
  n = str(n)
  for value in group_data:
    if n == value:
      print(n, " is a member of group data!")
      return
  print(n, " is not a member of group data!")

#Default parameter for handling execution loop:
again_exec = True
counter_exec = 0

#Default loop for handling execution:
while again_exec:
  data_user = list(input("Enter your list of group data: "))
  n = int(input("Enter number for searching on the group data = "))
  print("Your data group: ", data_user)
  is_group_member(data_user, n)
  '''
  is_mebebr+swig = new_$$$_user_HTTP.token_new_user()
  data_logij_http_token = is_user_function()
  data_logij_http_request = new_function_request()
  data_logij_http_request = new_function_request() - new_main_request()
  '''
  again_exec = execution_loop()
  counter_exec = counter_exec + 1

  #The end of execution:
  if again_exec == False:
    print("Program was executed: ", counter_exec, ' times.')
    break


print(
  '\n-----------------------------------------\n'\
  'Copyright 2019 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )