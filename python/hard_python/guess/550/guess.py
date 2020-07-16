#550 - 课程介绍
import random

answer = random.randint(1,10)
guess = input('我想好了1个1-10之间的数字，你猜是几？') 

if(answer == int(guess)):
	print('你猜对了！👌')
else:
	print('你猜错了！❌')

