factors = []

def getfactors(num):
	factor = num
	while factor>0:
		if num%factor==0:
			factors.append(factor)
		factor-=1


num = raw_input('Enter a num: ')
getfactors(int(num))
print factors