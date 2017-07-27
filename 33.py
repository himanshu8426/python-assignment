"""
PROGRAM ---33---
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
"""
input_file = raw_input("input file name =")
def semordnilap( file_name):
    try:
        with open( file_name) as file_object:
            word_list = file_object.read().split(" ")	
            to_print = list(filter(lambda word: word[::-1] in\
            word_list, word_list))
        return to_print
    except IOError:
        print "File not exist."

print semordnilap( input_file)
