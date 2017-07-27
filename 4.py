"""
PROGRAM ---4---
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""
str = raw_input("insert character =")
def check_vowel(str):
	vowel = ['a','e','i','o','u']
	if str in vowel:
		return True
	else :
		return False

print check_vowel(str)
