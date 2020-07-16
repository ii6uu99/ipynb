print(
  '-----------------------------------------\n'\
  'Practical python education || Exercise-24:\n'\
  '-----------------------------------------\n'
  )

print(
  'Task:\n'\
  '-----------------------------------------\n'\
  'Write a Python program to test whether a passed letter is a vowel or not.\n'
  )

print(
  'Solution:\n'\
  '-----------------------------------------'\
  )

def is_vowel(char):
  all_vowels = 'aeiou'
  return char in all_vowels

print(is_vowel(input("Please, enter your letter for checking out: ")))
print(is_vowel(input("Please, enter a new letter again for checking out:")))


print(
  '\n-----------------------------------------\n'\
  'Copyright 2018 Vladimir Pavlov. All Rights Reserved.\n'\
  '-----------------------------------------'
  )