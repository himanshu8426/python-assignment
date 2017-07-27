"""
PROGRAM ---27---
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
"""
listA = input('enter list of words =')
def map1(listA):
	listB =[]
	for word in listA:
		listB.append(len(word))
	return listB

#print map1(listA)


def map2(listB):
	return list(map(lambda x: len(x),listB))

#print map2(listA)

def map3(listA):
	return [len(word) for word in listA]

print map3(listA)
