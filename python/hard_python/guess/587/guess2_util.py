import random

#产生一个4位数字
def generate_answer():
	#return random.randint(1000, 9999)
	return 9527

def make_guess():
	return input('请输入猜测：')

#返回一个2A2B这样的字符串，有可能会抛出异常
def check_guess(answer, guess):
	guess = int(guess)
	a_num = check_guess_A(answer, guess)
	b_num = check_guess_B(answer, guess)
	result = f'{a_num}A{b_num}B'
	return result

#返回数字和位置都正确的个数
#例如:9527, 9572返回2
def check_guess_A(answer, guess):
	count = 0
	answer_str = str(answer)
	guess_str = str(guess)
	for index, char in enumerate(answer_str):
		if(guess_str[index] == char):
			count += 1
	return count

#如果数字正确，但位置不对就是B
#数字和位置都正确不算在内
#举例: 5923,9527，应该返回2
def check_guess_B(answer, guess):
	count = 0
	answer_str = str(answer)
	guess_str = str(guess)
	for index, char in enumerate(guess_str):
		if(char in answer_str and answer_str.index(char) != index):
			count += 1
	return count

#如果赢了返回True,否则返回False
def process_result(guess_count, guess, result):
	print(guess_count, guess, result)
	if(result == '4A0B'):
		print('Yeah! You Win!')
		return True
	return False

def show_scores():
	print('pass')

def should_continue():
	return False

if __name__ == '__main__':
	print('testing')
	assert(check_guess_A(9527, 9522)==3)  #断言
	assert(check_guess_A(9527, 9572)==2)  #断言
	assert(check_guess_A(9527, 9527)==4)  #断言
	assert(check_guess_A(9527, 9342)==1)  #断言
	assert(check_guess_A(9527, 7342)==0)  #断言
	assert(check_guess_B(9527, 5923)==2)  #断言
	assert(check_guess_B(9527, 5972)==4)  #断言



