#静态方法
#1. 需要使用@staticmethod 2. 不需要传入实例或者类作为第一个参数
class Dog:
	dogs = [] 

	@classmethod
	def num_of_dogs(cls):
		return len(cls.dogs)

	@classmethod
	def biggest(cls):
		max_height = -0.1
		for d in cls.dogs:
			if(d.height > max_height):
				max_height = d.height
		return max_height	
	
	@staticmethod
	def intro():
		print("Dog is human's best friend")

	def __init__(self, name, height, power):
		self.name = name 
		self.height = height
		self.power = power
		self.blood = 10
		Dog.dogs.append(self)
		print(f"{self.name}出生了，汪汪！")

	def bark(self):
		print(f'我是{self.name}，身高{self.height}, 血量{self.blood}，攻击力{self.power}')
	def attack(self, dog2):
		dog2.reduce_blood(self.power)
	def reduce_blood(self, reduce_value):
		if(reduce_value > self.blood):
			self.blood = 0
		else:
			self.blood = self.blood - reduce_value

d1 = Dog('大黄', 0.7, 3) 
d2 = Dog('二黑', 0.5, 4)

Dog.intro()
d1.intro()



