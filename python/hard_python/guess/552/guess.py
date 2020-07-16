#552 - 给点提示
import random

answer = random.randint(1,10)

while(True):
	guess = int(input('我想好了1个1-10之间的数字，你猜是几？')) 

	if(answer == guess):
		print('你猜对了！👌')
		print('游戏结束！886')
		break; #跳出循环
	elif(guess > answer):
		print('太大了，继续猜：')
	else:
		print('太小了，继续猜：')

