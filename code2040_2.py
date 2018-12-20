from functools import reduce

def maskify(cc):
	"""Returns a string with all but the last four characters changed to '#'"""
	if cc == "":
		return cc
	timesRepeat = len(cc) - 4
	return ('#'*timesRepeat + cc[timesRepeat:])

# a = maskify("5512103073210694")
# print(a)

def accum(s):
  """Returns modified string according to specifications in problem Instructions"""  
  if s == "":
    return s
  repeatRange = list(range(0, len(s)))
  repeatString = list (map (lambda x: repeat(s[x], x+1) + "-", repeatRange))
  upperCaseList = list (map (lambda x: x[0].upper() + x[1:], repeatString))
  output = (reduce (lambda x, y: x + y, upperCaseList))[:-1]
  return output
  
def repeat(s, x):
  """Repeats character x amount of times"""
  if x == 0:
    return s
  return s.lower()*x

# a = accum("NyffsGeyylB")
# print(a)

def valid_pin(input):
  """Returns whether input is a valid pin"""
  if input == "" or (len(input) != 4 and len(input) != 6):
    return False
  filteredString = list (map (lambda x: x.isdigit(), input))
  is_incorrectInput = list (filter (lambda x: x == False, filteredString))
  if is_incorrectInput == []:
    return True
  return False

# print(valid_pin("1346"))
