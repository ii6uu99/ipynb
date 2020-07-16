from guess2_util import *

while(True):
	#玩一轮
	generate_answer() 

	while(True):
		make_guess() #交卷
		check_guess() #批卷
		process_result() #结果处理
	show_scores()

	#要不要继续
	should_continue()








