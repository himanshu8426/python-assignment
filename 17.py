"""
PROGRAM ---17---
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored."""
str = raw_input("input a string to check palindrome")
def palindrome(str):
	i=0
	j = len(str)-1
	flag =0
	while i<=j :
		if (str[i].isalpha() == False or str[j].isalpha()==False):
			while ( str[i].isalpha() == False and i<=j):
				i = i+1
			while ( str[j].isalpha() == False and i<=j):
				j = j-1
		if (str[i].isalpha() and str[j].isalpha()):
			if str[i].lower() == str[j].lower():

				i = i+1
				j = j-1
			else:
				flag = 1
				break
	
	if(flag == 0):
		return "PALINDROME"
	else:
		return "NOT PALINDROME"
print palindrome(str)
