class Dog:
	def __init__(self, name, height, power):
		self.name = name 
		self.height = height
		self.power = power
		self.blood = 10
		self._secrect = 9527

	def bark(self):
		print(f'我是{self.name}，身高{self.height}')

#牧羊犬
class SheepDog(Dog):
	def __init__(self, name, height, power, num_of_sheeps):
		super().__init__(name, height, power)
		self.num_of_sheeps = num_of_sheeps
	def protect(self):
		print('我开始保护小羊啦！')

	def bark(self):
		print('我是牧羊犬，我骄傲！')
		super().bark()


#警犬
class PoliceDog(Dog):
	def __init__(self, name, height, power, ability):
		super().__init__(name, height, power)
		self.ability = ability

#宠物犬
class PetDog(Dog):
	def __init__(self, name, height, power, price):
		super().__init__(name, height, power)
		self.price = price

sd = SheepDog('牧羊犬1', 0.6, 4, 5)
sd.bark()


