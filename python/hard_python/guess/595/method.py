#传值vs传引用
#1. 基本类型是传值:复制一份，不影响原来的变量的值
#2. 复杂类型是传引用:传过去是变量的内存地址,所以要修改就都修改了
#3. 复杂类型如何传值

height = 1.58

def predict_height(height):
	"""预测将来的身高"""
	height = height + 0.3
	return height

future_height = predict_height(height)

# print(future_height)
# print(height)

heights = [1.58, 1.56, 1.87, 1.98]

def predict(heights):
	for index, h in enumerate(heights):
		heights[index] = h+0.3
	return heights

future_heights = predict(heights[:])
print(heights)
print(future_heights)

print(id(heights))
print(id(future_heights))







