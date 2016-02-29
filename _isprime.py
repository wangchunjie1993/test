def isprime(num):
	factor = num/2
	while factor>1:
		if num%factor==0:
			return False
		factor-=1
	else:
		return True


num = raw_input('Enter a num: ')
print isprime(int(num))