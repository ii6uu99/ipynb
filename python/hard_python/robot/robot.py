import openning as open
import order

#1. 出场
open.show_robot()

#2. 了解主人：问问题
name = open.ask()

while(True):
	print("-----------------")
	print("小麦：您有什么吩咐？")
	cmd = input() 
	if(cmd == 'time'):
		order.show_time()
	elif(cmd == 'hello'):
		order.hello(name) 
	elif(cmd == '88'):
		print('小麦：88，有需要再找我！')
		break;
	elif(cmd == 'tianqi'):
		order.tianqi('杭州')
	else:
	    print(order.ai_talk(cmd))		




