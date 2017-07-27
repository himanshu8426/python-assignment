"""
PROGRAM ---31---
Implement the higher order functions map(), filter() and reduce(). (They are built-in but writing them yourself may be a good exercise.)

"""
def __map__(func,list ):
	result = []
	for x in list:
		result.append(func(x))
	return result


def __reduce__(func,list ):
	a = list[0]
    n = len(list)
	for i in range(1,n):
		a = func(a,list[i])	
	return a

def __filter__(func ,list ):
	return [i for i in list if func(i) == True]



