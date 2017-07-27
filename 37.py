"""
PROGRAM ---37---
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""
input_file  = raw_input ("input =")
def file_set_number( file_name):
    try:   
        with open(file_name) as file_object:
            content = file_object.readlines()
    
        with open("37_new.txt","w+:") as file_new_object:
            for i in range(len(content)):
                file_new_object.write(str(i+1)+":"+content[i])
    except IOError:
        print "File does not exist!!!"

file_set_number(input_file )
