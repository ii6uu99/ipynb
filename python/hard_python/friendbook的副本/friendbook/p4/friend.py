from friend_data import mock_data
def print_usage():
	print("欢迎使用FriendBook，您可以输入以下命令：")
	print("list: 显示名单")
	print("张三：查询张三的情况，李四同理")
	print("886: 退出")

print_usage()
names, records = mock_data()
print(names)

while(True):
	cmd = input('请输入命令:')
	if(cmd == '886'):
		print("再见啦...")
		break
	elif(cmd == 'list'):
		print('名单如下....')
	else:
		print('张三....')



