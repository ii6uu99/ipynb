#类是一个模板
class Dog:
	#构造方法
	def __init__(self, name, height, power):
		self.name = name
		self.height = height
		self.power = power
		self.blood = 10

d1 = Dog('大黄', 0.7, 3) #创建第1个实例
d2 = Dog('二黑', 0.5, 4) #创建第2个实例

print(d1.name)
print(d2.name)

print(id(d1))
print(id(d2))
