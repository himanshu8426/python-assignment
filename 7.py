"""
PROGRAM ---7---
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
"""
str = raw_input("input a string + ")
def reverse_r( str ) :
	#str = input("input a string ")
	if len( str ) <= 1:
		return str
	
	return reverse(str[1:]) +str[0]
def reverse( str):
	n = len(str)
	str_rev = ""
	for i in range(n-1,-1,-1):
		str_rev += str[i]
	print str_rev
reverse( str )
