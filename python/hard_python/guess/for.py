# 561 For语法结构和基于数字(range)的循环
for x in range(5):
	print(x)

# 562 基于列表list，元祖tuple的循环
numbers = [3,4,5,8,2]
numbers2 = (6,7,2,5)
name = "zhangsan"
列表，元组，字典，集合，字符串等等
for x in name:
	print(x)

# 563 跳过单次循环
for x in [3,4,5,8,9]:
	if(x % 3 ==0):
		continue #跳过本次循环后面的语句，马上进入下一轮循环
	print(x)
	print(x*5)
	print(x*x)
	print(x*x*x)

# 564 马上退出所有循环
numbers = [3,4,5,8,9]
for x in numbers:
	if(x == 5):
		break #直接退出循环
	print(x)
print("程序结束了...")

#作业1: 写一个for循环，从1到100,
#如果是3的倍数输出‘麦’
#如果是5的倍数输出‘叔’
#如果又是3的倍数又是5的倍数，输出'Hello'
#其他都直接输出数字自己
#作业2：在1的基础上加上2个条件：
#1.如果是7的倍数就什么都不做。
#2.如果碰到66就退出。

# 565 嵌套循环
names = ['zhangsan','lisi','wangwu']
for name in names:
	for n in name:
		print(n)
	print("----")

# 566 一次性退出嵌套循环
names = ['zhangsan','lisi','wangwu']
is_found = False #表示是否找到了
for name in names:
	if(is_found):
		break
	for n in name:
		if(n == 's'):
			is_found = True
			break
		print(n)

# 567 显示循环的index和值
scores = [98,97,95,86,23]
for order, s in enumerate(scores, 1):
	print(order, s)

# 568 循环的本质-到底可以基于什么循环
for s in 'hello':
	print(s)
# 1. iterable	
# 2. iter('hello'): 'hello'.__iter__()，返回iterator
# 3. next(iterator): __next__()

# 569 实现自己的可循环类 - 随机数循环
import random
class RandomCount:
	def __iter__(self):
		return self
	def __next__(self):
		r = random.randint(1,10)
		if(r == 9):
			raise StopIteration
		return r

rc = RandomCount()
for s in rc:
	print(s)


# 570 再看While循环
# for循环的是iterable，适合一个具体的集合
# while适合根据条件判断
# 571 for else



