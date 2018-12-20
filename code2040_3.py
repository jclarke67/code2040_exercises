from functools import reduce
import functools
from operator import itemgetter

import collections

# if fields[9] not in {'A', 'D', 'E', 'N', 'R'}
# {'NORTH', 'SOUTH', 'EAST', 'WEST'}


def are_opposites(dir1, dir2):
	directions = {'NORTH', 'SOUTH', 'EAST', 'WEST'}

	if dir1 == 'NORTH':
		directions.remove('SOUTH')
		return True if dir2 not in directions else False

	elif dir1 == 'SOUTH':
		directions.remove('NORTH')
		return True if dir2 not in directions else False

	elif dir1 == 'EAST':
		directions.remove('WEST')
		return True if dir2 not in directions else False

	elif dir1 == 'WEST':
		directions.remove('EAST')
		return True if dir2 not in directions else False


def dirReduc(arr):
	output = ""
	# solved = None
	i = 0

	# While zero modifications have been made to current instance of list
	while check != 0:
		if i == len(arr)-1
		check = 0
		# If array contains only one direction

		if len(arr) == 1:
			return arr

		elif i+1 < len(arr):
			if are_opposites(arr[i], arr[i+1])
				output += ""
				check += 0
				i += 2

			else:
				solved = True
			output += new_addition
			return output

## If zero modifications have been made to list, the answer is correct

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
a = {'NORTH', 'SOUTH', 'EAST', 'WEST'}
b = 'NORTH'

print(type(a.add(a.remove('SOUTH'))))
print(a)
if b in a:
	print("TRUEEEEE")
else:
	print("FALSE SIR")


# def compareDir(dir1, dir2):
# 	if dir1 == "NORTH"
# 		if dir2 == "SOUTH"
# 			return "NO"
# 		if dir2 not in {'NORTH', 'EAST', 'WEST'}
# 	elif dir1 == "SOUTH"
# 		if dir2 == "NORTH"
# 			return "NO"
# 		if dir2 not in {'SOUTH', 'EAST', 'WEST'}

# 	elif dir1 == "NORTH"
# 		if dir2 == "SOUTH"
# 			return "NO"
# 	elif dir1 == "NORTH"
# 		if dir2 == "SOUTH"
# 			return "NO"






def is_isogram(string):
	if string != "":
		c = collections.Counter(string.lower()).most_common(1)
		return False if int(c[0][1]) > 1 else True
	return True

# a = "string"
# c = collections.Counter(x[0] for x in a.split() if x)
# c = collections.Counter(x[0] for x in ['s','t','r','i','n','g'] if x)

# c = is_isogram("")
# print(c)

def weightSort(x, y):
	val1 = (int(x[0]), int(x[1]))
	val2 = (int(y[0]), int(y[1]))
	if val1[0] > val2[0]:
		return 1
	elif val1[0] < val2[0]:
		return -1
	elif val1[0] == val2[0]:
		if val1[1] > val2[1]:
			print("THIS1: " + str(val1[1]) + "| THIS2: " + str(val2[1]))
			return 1
		else:
			print("ELSE1: " + str(val1[1]) + "| ELSE2: " + str(val2[1]))
			return -1

def calc_weight(amt):
	if len(amt) == 1:
		return int(amt)
	return reduce (lambda x, y: int(x) + int(y), amt)

def order_weight(strng):
	if strng == "":
		return ""
	strings = strng.split(' ')
	amtsWithWeights = list (map (lambda amt: (calc_weight(amt), amt + " "), strings))
	# print(amtsWithWeights)
	sortedAmtsWithWeights = sorted(amtsWithWeights, key=functools.cmp_to_key(weightSort))
	print(sortedAmtsWithWeights)
	sortedList = list (map (lambda pair: pair[1] , sortedAmtsWithWeights))
	b = sorted(sortedAmtsWithWeights, key=functools.cmp_to_key(weightSort))
	return (reduce (lambda x, y: x + y, sortedList))[:-1] 

# a = order_weight("16 38 95 1131268 49455 347464 59544965313 496636983114762 85246814996697 3 9")
# print(a)

# b = cmp=lambda x,y: cmp(x.lower(), y.lower())