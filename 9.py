"""
PROGRAM ---9---
Write a function is_member() that takes a value (i.e. a number, string, etc) x 
and a list of values a, and returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the in operator does,
 but for the sake of the exercise you should pretend Python did not have this operator.
 """
x = input("input a value =")
values = input("list input =")
def is_member(x, values ):
 	for value in values:
 		if value == x:
 			return True
 	return False
print is_member(x,values)
