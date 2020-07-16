#1. 首先创建100个Dog, 50个SheepDog, 50个PoliceDog
#2. 每一轮游戏，随机选出2个Dog
#3. dog1先攻击dog2，然后dog2攻击dog1
#3. 任何一方血量变为0就表明死亡！死亡的Dog退出游戏。
#4. 最后只有一个Dog了，游戏结束，胜利者可以吃鸡。
from dog import *
import random #产生随机数字
import time #时间模块

#1.创建100条狗
for i in range(100):
	if(i%2==0):
		SheepDog(i+1) #创建1个牧羊犬
	else:
		PoliceDog(i+1) #创建1个警犬

#2. 开始游戏循环
while(True):
	#判断是否只有1个Dog
	if(len(Dog.dogs) == 1):
		winner = Dog.dogs[0]
		print('🐔🐔🐔🐔🐔🐔🐔🐔')
		print('大吉大利，今晚吃鸡！')
		print(f'赢家是：{winner.dog_type()} {winner.name}')
		print('🐔🐔🐔🐔🐔🐔🐔🐔')
		break

	dog1, dog2 = random.sample(Dog.dogs, 2)
	dog1.attack(dog2)
	dog2.attack(dog1)
	time.sleep(0.02)
