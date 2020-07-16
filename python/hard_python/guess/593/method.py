#函数的3要素：名字, 参数，返回值
def bmi(height, weight):
	bmi_value = weight/(height*height)
	return round(bmi_value, 1)

print(bmi(1.83, 65))


def gongxi():
	print('恭喜发财！');

def hello(name, type):
	print(f"{name}是一个{type}")
hello('狗', '大黄')