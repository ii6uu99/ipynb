#函数的3要素：名字, 参数，返回值
def bmi(height, weight):
	"""计算BMI的值:
	   公式: 身高/(体重*体重)。
	   身高是以米为单位，如1.78
	   体重是以公斤为单位，如62公斤
	   函数返回计算好的BMI值，保留1位小数
	"""
	bmi_value = weight/(height*height)
	return round(bmi_value, 1)

print(bmi.__doc__)
print(round.__doc__)
#print(bmi(1.68, 72))