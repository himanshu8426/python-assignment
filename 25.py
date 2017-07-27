import re
"""
PROGRAM --25--

In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.

"""
w = input("input word =")
def is_vowel(x):
	vowel = ['a','e','i','o','u']
	if x in vowel:
		return True
	else:
		return False

def make_ing_form(word):
	length = len(word)
	if length >=3:
		x=word[length-1]
        	y=word[length-2]
        	z=word[length-3]
	flag =0
	if word.endswith('ie'):
		word = re.sub('e$','',word)
		word = re.sub('i$','y',word)
		word = word + "ing"
		flag =1
	elif word.endswith('e'):
                word = re.sub('e$','ing',word)
		flag = 1

	if flag ==0 and length >=3:
		if is_vowel(x)==False:
			if is_vowel(y)==True:
				if is_vowel(z)== False:
					word = word + word[length-1] + "ing"
					flag =1
	if flag ==0:
		word += "ing"
	
	return word

print make_ing_form( w )
