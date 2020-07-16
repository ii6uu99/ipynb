#传值vs传引用
#1. 函数就是一个对象，有自己的属性
#2. 可以被赋值
#3. 可以被传递
def bmi(height, weight):
	"体重指数计算方法"
	bmi_value = round(weight/(height*height),1)
	if(bmi_value < 18.5):
		return bmi_value, '多吃点'
	elif(bmi_value <= 24):
		return bmi_value, '你真棒！'
	else:
		return bmi_value, '多运动'

# is_fat = bmi
# print(is_fat.__name__)

def main(check):
	height = float(input('输入身高'))
	weight = float(input('输入体重'))
	print(check(height, weight))

main(bmi)



