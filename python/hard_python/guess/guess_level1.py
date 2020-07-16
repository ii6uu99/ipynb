import sys
import time #时间模块

def input_limit():
	try:
		limit = int(sys.argv[1]) #最多猜测次数
	except ValueError: #异常处理模块
		limit = 4
		print('输入次数有错，使用默认值：4')
	return limit

def calc_time(begin_time):
	end_time = time.time()
	used_time = end_time - begin_time #用了多少时间
	used_time = round(used_time, 2) #保留两位小数
	print(f'共用时{used_time}秒')	
	return used_time

def print_score(scores):
	best_score = min(scores, key=lambda x:x[2] if x[1] else 9999)
	print('=========战绩============')
	for _cycle, _is_right, _used_time in scores:
		label = '✌️ ' if(_is_right) else '❌ '
		best_label = '👄' if(_cycle == best_score[0] and best_score[1]) else '' #设定最好的标记
		print(f'{_cycle}轮，{label}，{_used_time}{best_label}')
	print('========================')