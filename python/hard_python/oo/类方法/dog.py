#类方法：可以通过类名调用，也可以通过实例名调用
#1.类方法不能访问实例变量，可以访问类变量 
#2.类方法需要加上@classmethod，第一参数必须是class (cls)
#作业: 1. 写一个方法num_of_big_dogs，这个方法返回所有height大于0.5的狗的数量
#2. 写一个方法smallest，这个方法返回最小的狗的身高
class Dog:
	#num_of_dogs = 0
	dogs = [] #用来保存所有狗的列表

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

	def __init__(self, name, height, power):
		self.name = name 
		self.height = height
		self.power = power
		self.blood = 10
		#Dog.num_of_dogs = Dog.num_of_dogs + 1
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

print(Dog.num_of_dogs())
print(d1.num_of_dogs())
print(d2.biggest())


