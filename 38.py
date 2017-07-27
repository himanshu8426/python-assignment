"""
PROGRAM ---38---
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).
"""
def avg_word_length(file_name ):
    try:
        with open(file_name ) as file_object:
            word_list = file_object.read().split()
            word_len_list = map(lambda word: len(word),word_list)
            length = reduce(lambda len_word1,len_word2: len_word1+len_word2,word_len_list)
            print length/len(word_list)
    except IOError:
        print "File does not exist!!!"
              
avg_word_length("38.txt")
	
