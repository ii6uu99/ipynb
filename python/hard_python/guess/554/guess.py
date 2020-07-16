#554 - 限制猜测次数for循环版本
import random

answer = random.randint(1,10)
guess_limit = 3 #最多猜测次数
is_right = False 

#while:根据一个判断条件；for是循环一个已知的列表 
for i in range(3):
	guess = int(input('我想好了1个1-10之间的数字，你猜是几？')) 
	if(answer == guess):
		is_right = True
		break;
	elif(guess > answer):
		print('太大了', end='，')
	else:
		print('太小了', end='，')

	if(i < guess_limit-1):
		print('请继续猜：')

#处理结果
if(is_right):
	print('你猜对了！👌')
	print('游戏结束！886')
else:
	print('你用完了猜测次数，你失败了❌')


