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

def ai_talk(question):
	return question.replace('你','我').replace('不','').replace('吗','').replace('?','!').replace('？','!')

def tianqi(city):
	url = 'http://t.weather.sojson.com/api/weather/city/101210101'
	import requests
	res = requests.get(url)
	tq_text = res.text
	import json
	tq_json = json.loads(tq_text)
	wendu = tq_json["data"]["wendu"]
	pm25 = tq_json["data"]["pm25"]
	print(f'{city}: 温度{wendu}度，pm2.5是{pm25}')

