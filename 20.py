# coding=utf-8
"""
PROGRAM ---20---
Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. That is, write a function translate() that takes a list of English words and returns a list of Swedish words."""
listA = raw_input("input a list to translate =")
def translate( listA ) :
	i = 0 
	dict1 = { "merry":"god" , "christmas":"jul" , "and":"och" , "happy":"gott" ,  "new":"nytt" , "year":"år"} 
	for word in listA:
		listA[i] = dict1[word]
		i = i+1
	return listA
	
listA = translate(listA)
print listA
