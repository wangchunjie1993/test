primeFactors = []

def isprime(num):
	factor = num/2
	while factor>1:
		if num%factor==0:
			return False
		factor-=1
	else:
		return True

def getPrimeFactors(num):
	while not isprime(num):
		factor = 2
		while factor<num:
			if isprime(factor) and num%factor==0:
				primeFactors.append(factor)
				num/=factor
				break
			factor+=1
	primeFactors.append(num)

num = raw_input('Enter a num: ')
getPrimeFactors(int(num))
print primeFactors
