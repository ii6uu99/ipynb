#2种狗具有不同的攻击力和防御能力。攻击强的防御弱；反之亦然；
import random
class Dog:
	dogs = [] #保存所有活着的Dog
	def __init__(self, name):
		self.name = name 
		self.blood = 100
		self.attack_power = 5
		self.defense_power = 3

	#攻击!
	def attack(self, dog2):
		print(f'{self.name}攻击{dog2.name}，攻击力:{self.attack_power}，防御力:{dog2.defense_power}')
		point = self.attack_power - dog2.defense_power
		if(dog2.blood > point):
			dog2.blood -= point
			print(f'{dog2.name}受到攻击，奋力自救，血量减少为{dog2.blood}')
		else:
			dog2.blood = 0
			print(f'{dog2.name}受到攻击，失血过多，死亡！😭😭😭😭😭😭😭😭')
			Dog.dogs.remove(dog2)	
	
	#判定狗的类型
	def dog_type(self):
		if(isinstance(self, SheepDog)):
			return '牧羊犬🐑'
		elif(isinstance(self, PoliceDog)):
			return '警犬👮'
		else:
			return '普通犬'


#牧羊犬
class SheepDog(Dog):
	def __init__(self, name):
		super().__init__(name)
		self.attack_power = random.randint(5, 10)
		self.defense_power = random.randint(3,5) 
		print('🐑牧羊犬{self.name}问世！')
		self.dogs.append(self)


#警犬
class PoliceDog(Dog):
	def __init__(self, name):
		super().__init__(name)
		self.attack_power = random.randint(8, 13)
		self.defense_power = random.randint(1,3) 
		print('👮‍♀️警犬{self.name}问世！')
		self.dogs.append(self)




