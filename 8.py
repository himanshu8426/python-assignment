"""
PROGRAM ---8---
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
"""
str = raw_input("input a word = ")
def palindrome( str ):
	n = len(str)
	i = 0	
	j= (n-1)
	flag =0
	while i<=j:
		if str[i] == str [j]:
			i=i+1
			j=j-1
			continue
		if str[i] != str[j]:
			flag = 1
			break
	if (flag == 0 ):
		return "PALINDRMOE"
	else:
		return "NOT PALINDORME"

print palindrome( str )
		
