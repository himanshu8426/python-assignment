"""
PROGRAM ---21---
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")."""
str = input("input a string =")
def char_freq( str ):
	dict = {}
	for char in str:
		if char in dict:	
			dict[char] = dict[char] +1
		else :
			dict[char] = 1
	
	for word in dict:
		print word," : ",dict[word]

char_freq(str)

