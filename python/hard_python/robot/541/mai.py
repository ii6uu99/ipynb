import openning as open
from datetime import datetime

#1. 出场
open.show_robot()

#2. 了解主人：问问题
name = open.ask()

while(True):
	print("小麦：您有什么吩咐？")
	cmd = input()
	print("小麦：知道了，已经做好了!")

#3. 问好
open.hello(name) 

#4.显示时间
dt = datetime.now()
print(dt.strftime('今天是:%Y年%m月%d日 %H:%M:%S'))



