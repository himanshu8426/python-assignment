"""
PROGRAM ---36---
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.
"""
import re
def hapax(file_name):
    try:
        with open(file_name) as file_object:
            word_list = file_object.read().split()
            freq = {key : 0 for key in word_list}
            for word in word_list:
                freq[word] += 1
            hapax_list = filter(lambda word: freq[word] == 1  ,word_list)
            print hapax_list
    except IOError:
        print "File not found"

hapax("36.txt")
