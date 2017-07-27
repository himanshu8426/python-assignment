"""
PROGRAM ---34---
Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.
"""
filename = raw_input ("input file name = ")
def char_freq_table ( file_name ):
    char_list =[]
    try:
        with open( file_name) as file_object:
            map(char_list.extend,file_object)
        char_list.sort()
        char_freq = [char_list.count(char) for char in char_list]
        return dict(zip(char_list,char_freq))
    except IOError:
        print "File does not exist!!!"
print char_freq_table(filename )
