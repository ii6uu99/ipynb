from datetime import datetime

robot_name = '小麦'
def show_time():
	dt = datetime.now()
	print(dt.strftime('今天是:%Y年%m月%d日 %H:%M:%S'))

#定义1个函数
def hello(name):
	print('---------------')
	print(f'你好，{name}，我是{robot_name}') 
	print(f"天地之间，{name}最帅！")
	print(f'我对{name}的敬仰之情，犹如黄河之水一发而不可收拾！')
	print(f'帅归帅，{name}出门别忘记带口罩！')