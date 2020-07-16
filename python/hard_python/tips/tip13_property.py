class Person:
	def __init__(self, age):
		self.age = age

class Person2:
	def __init__(self, age):
		self._age = age 

	def set_age(self, age):
		if(age > 100):
			self._age = 100
		else:
			self._age = age
		
	def get_age(self):
		if(self._age > 18):
			return 28
		else:
			return self._age

class Person3:
	def __init__(self, age):
		self._age = age 

	@property
	def age(self):
		if(self._age > 18):
			return 28
		else:
			return self._age

	@age.setter
	def age(self, age):
		if(age > 100):
			self._age = 100
		else:
			self._age = age

class Person4:
	def __init__(self, age):
		self._age = age 

	def set_age(self, age):
		if(age > 100):
			self._age = 100
		else:
			self._age = age
		
	def get_age(self):
		if(self._age > 18):
			return 28
		else:
			return self._age

	age = property(get_age, set_age)

zs = Person4(13)
print(zs.age )
zs.age = 888
print(zs.age)
#age是一个public属性

#封装，多态和继承！