"""
PROGRAM ---44---
Your task in this exercise is as follows:

Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK
"""
input_string = raw_input()
def balanced(string):
    stack = []
    for char in string:
        if char == "[" :
            stack.append("[")
        else:
            if len(stack) == 0:
                print "NOT OK"
                return
            else:
                stack.pop()
    to_print = "NOT OK" if len(stack) !=  0 else "OK"
    print to_print
balanced(input_string)
