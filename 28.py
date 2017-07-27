"""
PROGRAM ---28---
Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
"""
listA = input("list input of word =")
def find_longest_word(listA):
	return len(reduce(lambda x,y :x if len(x)>len(y) else y,listA ))

print find_longest_word(listA)
