"""
PROGRAM ---12---
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******
"""

listA = [4,9,7]
def histogram (listA):
	c ='*'
	for i in listA:
		print c*i

histogram(listA)
