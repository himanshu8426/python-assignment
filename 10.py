"""
PROGRAM ---10---
Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.
"""
list1 = input("list1 =")
list2 = input("list2 =")
def overlapping(list1 ,list2):
	for x in list1:
		for y in list2:
			if  x==y:
				return True
	return False
print overlapping(list1,list2)

