"""
PROGRAM ---26---
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
"""
listA = input('list input =')
def max_in_list(listA):
	return reduce(lambda x,y : x if (x>y) else y,listA)

print max_in_list(listA)

