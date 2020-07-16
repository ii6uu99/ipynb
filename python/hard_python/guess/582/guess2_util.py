import random

#产生一个4位数字
def generate_answer():
	return random.randint(1000, 9999)

def make_guess():
	return input('请输入猜测：')

#返回一个2A2B这样的字符串，有可能会抛出异常
def check_guess(answer, guess):
	guess = int(guess)
	a_num = check_guess_A(answer, guess)
	b_num = check_guess_B(answer, guess)
	result = f'{a_num}A{b_num}B'
	print(result)
	return result

def check_guess_A(answer, guess):
	return 2

def check_guess_B(answer, guess):
	return 2

#如果赢了返回True,否则返回False
def process_result():
	return True

def show_scores():
	print('pass')

def should_continue():
	return False

