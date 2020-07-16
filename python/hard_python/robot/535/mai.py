import openning as open
from datetime import datetime
import time

#1. 出场
open.show_robot()

time.sleep(1)

#2. 了解主人：问问题
#name = open.ask()

#3. 问好
#open.hello(name) 

#4. 显示时间：今天是：2020年2月29日 11:23:35
dt = datetime.now()
#print(f'今天是:{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}')
print(dt.strftime('今天是:%Y年%m月%d日 %H:%M:%S'))



