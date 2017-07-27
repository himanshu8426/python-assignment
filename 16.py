'''
PROGRAM ---16---
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
'''
listA = input("list input =")
n = input ("n = ")
def filter_long_words(listA , n):
	listB = []
	for word in listA:
		length = len(word)
		if length >= n:
			listB.append(word)

	return listB
listB = filter_long_words(listA,n)
print listB
