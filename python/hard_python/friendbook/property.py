class Person:
	def __init__(self, age):
		self.age = age

zs = Person(23)

zs.age = 24
print(zs.age)

class Cat:
	def __init__(self, age):
		self._age = age
	
	@property
	def age(self):
		return self._age

	@age.setter    
	def age(self, new_age):
		self._age = new_age

	nianling = property()

c = Cat(5)
c.age = 19
print(c.age)
