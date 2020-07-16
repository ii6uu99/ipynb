import openning as open

name = input('我是小麦，你叫什么名字？\n') 
age = input('我8岁了，你呢？\n') #age是一个字符串str
age = int(age)

#1. 顺序很重要
if(age < 50): 
	print(f"{age}岁像一座沉稳的大山！")
elif(age < 30): 
	print(f"{age}岁如花似玉的年龄！")
else:
	print(f"{age}岁有丰富的人生阅历！")

#2. 语句块可以嵌套


#open.icon()
#open.hello(name) 





