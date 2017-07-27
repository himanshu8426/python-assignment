from collections import defaultdict
"""
PROGRAM ---43---
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them.
"""
"""
f = open("43.txt")
line = f.readlines()
wordlist =[]
sortedwl =[]
for word in line:
	wordlist.append(word[0:-1])
for word in wordlist:
	sortedwl.append(sorted(word))
n = len(wordlist)
for i in range(n):
	word1= sortedwl[i]
	k=i+1
	for j in range(k,n) :
		word2=sortedwl[j]
		if word1 == word2:
			print wordlist[i],wordlist[j]
"""
try:
    with open("43.txt") as file_object :
        word_list = file_object.read().splitlines()
    count = 0
    sorted_word_list = (map(lambda word: ''.join(sorted(word)),word_list))
    for index1 in range(len(word_list)):
        flag = 0
        word1 = sorted_word_list[index1]
        k = index1 + 1
        for index2 in range(k,len(word_list)):
            word2 = sorted_word_list[index2]
            if word1 == word2:
                flag = 1
                print word_list[index1],word_list[index2]
        if flag == 1:
            count += 1

            
    print count
except IOError:
    print "File not found"

