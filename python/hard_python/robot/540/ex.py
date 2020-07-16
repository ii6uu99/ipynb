#作业：实现一个闰年的函数
def run_nian(year):
	return (year%4==0 and year%100!=0) or year%400==0

#断言: 4个测试用例
assert run_nian(2004)==True
assert run_nian(2005)==False
assert run_nian(2000)==True
assert run_nian(2100)==False

#Bool的推测规则：
#1. 数字0是False, 其他为True
#2. 空的字符串''是False, 其他为True
#3. None是False
#4. 空的元祖，列表，字典为False, 其他为True
if(None):
	print(1)