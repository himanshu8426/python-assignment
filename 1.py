"""
PROGRAM ---1---
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""
a = input("a=")
b = input("b=")
def max(a , b):
	if (a > b):
	 	print ("a is greater which is "+ str(a))
	elif (b > a):
         	print ("b is greater which is "+ str(b))
	else :
		print "equal"
max(a,b)
