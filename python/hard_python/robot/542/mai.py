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
	else:
	    print('我还不是万事通，但我在努力学习中..')		




