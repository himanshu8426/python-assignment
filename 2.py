"""
PROGRAM ---2---
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""
a = input("a=")
b = input("b=")
c = input("c=")
def max_of_three(a,b,c):
	if (a>b):
		if(a>c):
		 print a
		else:
		 print c
	else:
		if(b>c):
		 print b
		else:
		 print c

max_of_three(a,b,c)

