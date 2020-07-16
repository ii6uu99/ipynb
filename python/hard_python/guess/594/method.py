#返回值：
#1. 可以有返回值，也可以没有，None.
#2. 返回值通过return来返回
#3. 一旦遇到return，函数执行接结束了
#4. 如果返回多个值，多个值被包在一个元祖里
def bmi(height, weight):
	bmi_value = round(weight/(height*height),1)
	if(bmi_value < 18.5):
		return bmi_value, '多吃点'
	elif(bmi_value <= 24):
		return bmi_value, '你真棒！'
	else:
		return bmi_value, '多运动'

result = bmi(1.83, 65)
bmi_value, msg = bmi(1.83, 65)

print(result[0])


def send_flower(flower_num):
	if(flower_num < 10):
		return '今天有事，以后再联系！'
	if(flower_num % 14 == 0):
		return '今天有时间吗？晚上一起吃饭'
	else:
		return '谢谢你！'

#print(send_flower(28))

