class MyBase(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print 'MyBase instance created'


class MyDerive(MyBase):
	def __init__(self,name= 'DefaultName',age = 'DefaultAge'):
		#	MyBase.__init__(self,name,age)
		super(MyDerive,self).__init__(name,age)
		print 'MyDerive instance created'
	pass

a = MyBase('Alex',23)
#b = MyDerive('Bob',10) 	 	
b = MyDerive()
print b.name

print 

class TestStaticMethod(object):
	@staticmethod
	def foo():
		print 'calling static method "foo"'

#	foo = staticmethod(foo)

class TestClassMethod(object):
	@classmethod
	def foo(cls):
		print 'calling class method "foo"'

#	foo = classmethod(foo)


TestStaticMethod.foo()
TestClassMethod.foo()
