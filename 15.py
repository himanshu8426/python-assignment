"""
PROGRAM ---15---
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""
listA = input("list input = ")
def find_longest_word( listA):
	n = len (listA)
	longest = len(listA[0])
	index = 0
	for i in range(1,n):
		length =len( listA[i])
		if length > longest:
			longest = length
			index = i
	return listA[index]
print find_longest_word(listA)
