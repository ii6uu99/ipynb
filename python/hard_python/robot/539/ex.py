#作业：实现一个闰年的函数
def run_nian(year):
	return (year%4==0 and year%100!=0) or year%400==0

#断言: 4个测试用例
assert run_nian(2004)==True
assert run_nian(2005)==False
assert run_nian(2000)==True
assert run_nian(2100)==False