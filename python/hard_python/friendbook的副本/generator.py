#Python Generator
#1. 什么是Generator: 是一个生成器，可以生成1个个东西，通过next()，是一个iterable
#2. 为什么要用Generator？列表很大的时候，Generator按需给你产生，不会一次性生成而占用大量内存
import memory_profiler as mem

#最简单的例子
nums = [1,2,3,4,5]
squre_nums = (n*n for n in nums)

#数量大一点
yi = 100000000
# nums = list(range(10000000))
# print(f'内存前：{mem.memory_usage()}')
# #squre_nums = [n*n*yi for n in nums]
# squre_nums = (n*n*yi for n in nums)
# print(f'内存后：{mem.memory_usage()}')


#yield的例子

def calc_nums(nums):
	new_nums = []
	for n in nums:
		if(n%3==0):
			new_nums.append(3*yi) 
		elif(n%5==0):
			new_nums.append(5*yi) 
		else:
			new_nums.append(n*yi) 
	return new_nums

def gen_nums(nums):
	for n in nums:
		if(n%3==0):
			yield 3*yi 
		elif(n%5==0):
			yield 5*yi
		else:
			yield n*yi

nums = list(range(10))
cnums = calc_nums(nums)
gnums = gen_nums(nums)
print(gnums)
for n in gnums:
	print(n)

#yield 
#进程，线程，协程




