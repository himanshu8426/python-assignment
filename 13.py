"""
PROGRAM ---13---
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.
"""
listA = input("input list = ")
def max_in_list(listA):
	mn = float('-inf')
	for i in listA:
		if mn < i:
			mn = i
	return mn

print max_in_list(listA)

