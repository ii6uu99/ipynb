print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-22:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to count the number 4 in a given list."\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print("Number of 4 in the list: 3, 5, 4, 1, 2, 4, 9, 0, 4, 4, 4, 8, 5, 1, 4, 8, 4 = ");
print(list_count_4([3, 5, 4, 1, 2, 4, 9, 0, 4, 4, 4, 8, 5, 1, 4, 8, 4]))
print("Number of 4 in the list: 0, -2, -8, -9, 4, 8, -3, 4, -6, -255, 44, 4")
print(list_count_4([0, -2, -8, -9, 4, 8, -3, 4, -6, -255, 44, 4]))


print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )