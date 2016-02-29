db = {}

def newuser():
	while True:
		name = raw_input('Enter user name: ')
		if name in db:
			print 'User name exist!'
			continue
		else:
			db[name] = raw_input('Enter password: ')
			break

def olduser():
	while True:
		name = raw_input('Enter user name: ')
		if name not in db:
			print 'User name not exist!'
			continue
		else:
			while True:
				pwd = raw_input('Enter password: ')
				if pwd!=db[name]:
					print 'Password incorrect!'
					continue
				else:
					break
			break

def showmenu():
	prompt = """ 
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter your choice:"""
	while True:
		try:
			choice = raw_input(prompt).strip()[0].lower()
		except(EOFError,KeyboardInterrupt):
			choice = 'q'

		if choice not in 'neq':
			print 'invalid option,try again'
			continue

		if choice == 'n':
			newuser()
		elif choice == 'e':
			olduser()
		elif choice == 'q':
			break


if __name__ == '__main__':
	showmenu()
