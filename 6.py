"""
PROGRAM ---6---
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""
sumn = [1,2,3,4]
muln = [1,2,3,4]

def sum( sumn ):
	count = 0
	for i in sumn:
		count = count + i
	return count
def mul( muln ): 
	count  = 1
	for i in muln:
		count = count * i	
	return count

print sum(sumn)
print mul(muln)

