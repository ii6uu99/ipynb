#类是一个模板
class Dog:
	#构造方法
	def __init__(self, name, height, power):
		self.name = name
		self.height = height
		self.power = power
		self.blood = 10
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

d1.reduce_blood(4)
d1.reduce_blood(4)
d1.reduce_blood(4)
d1.bark()


