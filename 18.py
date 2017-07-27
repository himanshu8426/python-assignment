"""
PROGRAM ---18---
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not."""
str = raw_input("Input a string to check Panagram =")
def panagram ( str ):
	dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
	for char in str:
		c = char.lower()
		dict[c] = 1
	flag =0
	for word in dict:
		if dict[word] == 0:
			flag = 1
			break		
	if (flag  == 0):
		return "PANAGRAM"
	else:
		return "NOT PANAGRAM"

print panagram (str)

