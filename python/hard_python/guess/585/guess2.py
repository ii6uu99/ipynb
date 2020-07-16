from guess2_util import *

next_cyle = True
while(next_cyle):
	#玩一轮
	answer = generate_answer() 
	win = False
	while(not win):
		try:
			guess = make_guess() #交卷
			result = check_guess(answer, guess) #批卷 2A2B
			win = process_result() #结果处理
		except ValueError:
			print('输入错误，请输入4位数字')
		except IndexError:
			print('输入数字位数错误，必须是4位数字')


	show_scores()

	#要不要继续
	next_cyle = should_continue()








