import openning as open

#1.输入姓名
name = input('我是小麦，你叫什么名字？\n') 
age = input('我8岁了，你呢？\n') #age是一个字符串str

#类型转换
age = int(age)

#判断：
#如果age大于30：我喜欢成熟的人，很有魅力；
#如果age小于30：你真年轻，如花似玉的年龄；
#语句块
if(age < 30): 
	print(f"你才{age}啊！")
	print("你真年轻，如花似玉的年龄!")
elif(age < 50): 
	print(f"{age}岁像一座沉稳的大山！")
else:
	print(f"{age}岁有丰富的人生阅历！")


#open.icon()
#open.hello(name) 





