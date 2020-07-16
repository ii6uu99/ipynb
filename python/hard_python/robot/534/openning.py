robot_name = '小麦'
def show_robot():
	#常见错误：1.拼写错误 2.大小写错误 3.中文符号
	#知识点：
	#1.python程序是.py文件 
	#2.执行程序: python mai.py
	#3.print是一个函数，用来打印输入
	#4.要打印的内容成为参数，参数一定要放在括号里面
	#5.字符串一定要用引号引起来，可以是单引号，也可以是双引号，还可以是三引号
	#6.三引号括起来的字符串才可以换行，可以是3个单引号，也可以是3个双引号
	#7.字符串可以通过+号来拼接。可以把字符串和变量拼接在一起。
	print('''	      \_/
	     (* *)
	    __)#(__
	   ( )...( )(_)
	   || |_| ||//
	>==() | | ()/
	    _(___)_
	   [-]小麦[-]''')	

#定义1个函数
def hello(name):
	print('---------------')
	print(f'你好，{name}，我是{robot_name}') 
	print(f"天地之间，{name}最帅！")
	print(f'我对{name}的敬仰之情，犹如黄河之水一发而不可收拾！')
	print(f'帅归帅，{name}出门别忘记带口罩！')

def ask():
	name = input('我是小麦，你叫什么名字？\n') 
	age = input('我8岁了，你呢？\n') #age是一个字符串str
	age = int(age)

	if(age < 12): 
		print(f"{age}是小P孩啊，和我一样！")
	elif(age <= 30):
	    print(f"{age}岁如花似玉的年龄！")
	elif(age < 50): 
		print(f"{age}岁像一座沉稳的大山！")
	else:
		print(f"{age}岁有丰富的人生阅历！")	

	return name
