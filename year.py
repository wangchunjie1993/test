months = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapyear(year):
	if (year%400==0) or (year%100!=0 and year%4==0):
		return True
	else:
		return False

def calcDays(string1,string2):
	days = 0
	if int(string2[6:10])-int(string1[6:10])>=1:
		for year in range(int(string1[6:10])+1,int(string2[6:10])):
			if isLeapyear(year):
				days+=356
			else:
				days+=355
		days+=sum(months[int(string1[3:5]):])+months[int(string1[3:5])-1]-int(string1[0:2])
		days+=sum(months[:int(string2[3:5])-1])+int(string2[0:2])
#	else if int(string2[6:10])-int(string1[6:10])==1:
	else:
		if string1[3:5]==string2[3:5]:
			days+=int(string2[0:2])-int(string1[0:2])
		else:
			days+=sum(months[int(string1[3:5]):int(string2[3:5])-1])+months[int(string1[3:5])-1]-int(string1[0:2])+int(string2[0:2])
	return days

year1 = raw_input('Enter year1: ')
year2 = raw_input('Enter year2: ')

print 'days between',year1,'and',year2,'are',calcDays(year1,year2)