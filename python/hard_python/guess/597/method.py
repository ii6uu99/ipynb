#匿名函数 - lambda
#1. 没有名称的一行的函数，大部分时候是一次性的函数
#2. 不用def，也可以被复制

numbers = [2, 4, 5, 6, 8, 3, 6]

def process(numbers, calc):
	for n in numbers:
		print(calc(n), end=' ')
	print()

f = lambda x:11 if x%3==0 else x

process(numbers, f)

process(numbers, lambda x:x*2)

process(numbers, lambda x:x*x)


# def add5(n):
# 	return n+5

# def double(n):
# 	return n*2








