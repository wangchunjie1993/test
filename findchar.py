def findchar(string,char):
	i = 0
	for item in string:
		if item==char:
			return i
		i+=1

def subchr(string,origchar,newchar):
	newlist = list(string)
	i=0
	for c in newlist:
		if c==origchar:
			newlist[i]=newchar
		i+=1
	return ''.join(newlist)

string = raw_input('Enter a string: ')
origchar = raw_input('Enter the origchar: ')
newchar = raw_input('Enter the newchar: ')
#print findchar(string,char)

print subchr(string,origchar,newchar)


