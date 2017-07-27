"""
PROGRAM ---32---
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.
"""
from file8 import palindrome
input_file = raw_input("input a file name: ")

def palindrome_of_file(input_filename ):
	with open(input_filename) as input_file_object:
		word_list = list(input_file_object.read().split("\n"))
	return filter(lambda word: palindrome(word) == True,word_list)

print palindrome_of_file(input_file)
