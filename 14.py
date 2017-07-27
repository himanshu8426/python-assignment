"""
PROGRAM ---14---
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""
listA = input("input list =")
lengths = []
def map_of_list_length( listA ):
	for word in listA:
		lengths.append(len(word))
	return lengths

lengths = map_of_list_length( listA )
print lengths

