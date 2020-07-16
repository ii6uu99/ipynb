#572 - try except; 
import random
import time #时间模块
from guess_level1 import *

#1.输入次数限制
guess_limit = input_limit() 

#2.准备数据结构
scores = [] #战绩
cycle = 0 #第几轮

#3. 开始1轮游戏
while(True):
	cycle += 1

	#3.1 生成答案
	answer = random.randint(1,1)

	is_right = False 
	begin_time = time.time()
	
	#3.2 进行猜测 
	for i in range(guess_limit):

		#3.2.1 输入猜测
		try:
			guess = int(input('我想好了1个1-10之间的数字，你猜是几？')) 
		except:
			print('别乱说，输入1-10之间的数字')
			continue

		#3.2.2 判断答案
		if(answer == guess):
			is_right = True
			break;
		elif(guess > answer):
			print('太大了', end='，')
		else:
			print('太小了', end='，')

		if(i < guess_limit-1):
			print('请继续猜：')

	#3.3. 处理最终处理结果
	if(is_right):
		print('你猜对了！👌')
	else:
		print('你用完了猜测次数，你失败了❌')

	#3.4 处理时间和显示战绩
	used_time = calc_time(begin_time)
	scores.append((cycle, is_right, used_time))
	print_score(scores)

	#3.5 判断是否继续玩下去
	con = input('要继续玩，输入y，否则直接回车：')
	if(con != 'y'):
		print('886...')
		break #退出游戏






