#定义1个函数
def hello(name, robot_name):
	print('你好，' + name + '，我是' + robot_name) 
	print('天地之间，' + name + '最帅！')
	print('我对' + name + '的敬仰之情，犹如黄河之水一发而不可收拾！')
	print('帅归帅，' + name + '出门别忘记带口罩！')

	#1.如果有多个参数传给一个函数，用逗号隔开
	#2.可以通过{}表示变量，然后通过format函数传入要填入的变量
	print('---------------')
	print('你好，{}，我是{}'.format(name,robot_name)) 
	print("天地之间，{}最帅！".format(name))
	print('我对{}的敬仰之情，犹如黄河之水一发而不可收拾！'.format(name))
	print('帅归帅，{}出门别忘记带口罩！'.format(name))

	#1.语法糖衣：只是一种比较简单的写法，本质的一样的
	#2.可以在字符串前加上f，然后在字符串中只用{name}自动拼接内容
	print('---------------')
	print(f'你好，{name}，我是{robot_name}') 
	print(f"天地之间，{name}最帅！")
	print(f'我对{name}的敬仰之情，犹如黄河之水一发而不可收拾！')
	print(f'帅归帅，{name}出门别忘记带口罩！')

	#1.print可以接受多个参数，自动打印出来，并且默认用空格隔开
	print('---------------')
	print('你好，',name, '，我是', robot_name) 
	print('天地之间，', name,  '最帅！')
	print('我对', name, '的敬仰之情，犹如黄河之水一发而不可收拾！')
	print('帅归帅，', name, '出门别忘记带口罩！')

	#转义字符
	#1. 单引号里可以包含双引号；双引号里可以包含单引号；三引号里面可以放任何东西
	#2. \表示转移字符，它告诉Python\后面的字符是一个普通字符，不要去解析它
	print('what\'s your name')

	#1. 最重要的技能是自己会查文档：print文档查询
	#2. 可以指定分隔符 sep=  3.可以指定结尾符
	print(1,2,3,4,5,sep='|', end=' ')
	print(1,2,3,4,5,sep='|')