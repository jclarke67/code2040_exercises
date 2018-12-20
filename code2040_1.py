from functools import reduce

def toCapCase(string):
  if string == "":
    return string
  strings = string.split(' ')
  modifiedStrings = list (map (lambda x: x[0].upper() + x[1:], strings))
  modifiedSentence = reduce((lambda x, y: x + " " + y), modifiedStrings)
  return modifiedSentence

a = toCapCase("How can mirrors be real if our eyes aren't real")
print(a)

def solution(number):
  """Returns the sum of all the multiples of 3 or 5 below the number passed in."""
  if number == 0:
    return 0
  numberRange = list(range (number)) 
  multiples3 = list (map (lambda x: x*3, numberRange))
  multiples3 = list(filter(lambda x: x < number, multiples3))
  multiples5 = list (map (lambda x: x*5, numberRange))
  multiples5 = list(filter(lambda x: x < number, multiples5))
  total = reduce((lambda x, y: x + y), list(set(multiples3 + multiples5)))
  return total

# print(solution(0))

