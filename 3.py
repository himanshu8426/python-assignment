"""
PROGRAM ---3---
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""
def length( str ):
	count = 0
	for letter in str:
		count = count + 1
	print count
list1 = ['banana', 'apple', 'mango']
str1 ="abcdefghi"
length(str1)	
length(list1)
