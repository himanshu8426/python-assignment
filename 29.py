"""
PROGRAM ---29---
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""
listA = input  ("input word = ")
n = input("n = ")
def filter_long_word( listA , n):
	return list(filter(lambda x: len(x)>n,listA ))

print filter_long_word(listA,n)
