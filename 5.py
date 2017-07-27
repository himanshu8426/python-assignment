# -*- coding: utf-8 -*-
"""
PROGRAM ---5--
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""
str = raw_input("enter string = ")
def transalte( str ):
	vowel = ['a','e','i','o','u',' ']
	str1 = ""
	for char in str:
		if char not in vowel:	
			str1 = str1 + char +  'o'+ char
		else :
			str1 = str1 + char 
	return str1
print transalte(str)
