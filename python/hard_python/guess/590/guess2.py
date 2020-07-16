from guess2_util import *
import time

scores = [] #保存每一轮的结果
cycle_count = 0 #记录游戏的轮次
next_cyle = True
while(next_cyle):
	cycle_count += 1
	begin_time = time.time()

	#玩一轮
	answer = generate_answer() 
	win = False
	guess_count = 0
	while(not win):
		try:
			guess = make_guess() #交卷
			result = check_guess(answer, guess) #批卷 2A2B
			guess_count += 1
			win = process_result(guess_count, guess, result) #结果处理
			if(win):
				end_time = time.time()
				used_time = int(end_time - begin_time)
				scores.append((cycle_count, guess_count, used_time))
		except ValueError:
			print('输入错误，请输入4位数字')
		except IndexError:
			print('输入数字位数错误，必须是4位数字')

	#显示每一轮的成绩，比如：
	#轮次, 猜测次数, 使用时间
	show_scores(scores)

	#要不要继续
	next_cyle = should_continue()








