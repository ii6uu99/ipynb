#类是一个模板
class Dog:
	num_of_dogs = 0 #类属性

	#构造方法 - 添加实例属性，做其他的初始化工作
	def __init__(self, name, height, power):
		self.name = name 
		self.height = height
		self.power = power
		self.blood = 10
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

d1 = Dog('大黄', 0.7, 3) #创建第1个实例
d2 = Dog('二黑', 0.5, 4) #创建第2个实例

d1.num_of_dogs = 10 #给d1创建了一个实例属性，当实例属性和类属性相同时，通过实例访问，优先访问的是实例属性
Dog.num_of_dogs = 8
print(Dog.num_of_dogs) #通过类名访问
print(d1.num_of_dogs) #通过实例访问
print(d2.num_of_dogs)


