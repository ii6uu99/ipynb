from cmd.friend_list import show_list, find, find_by_id
def print_usage():
	print("欢迎使用FriendBook，您可以输入以下命令：")
	print("list: 显示名单")
	print("张三：查询张三的情况，李四同理")
	print("886: 退出")

print_usage()

while(True):
	cmd = input('请输入命令:')
	if(cmd == '886'):
		print("再见啦...")
		break
	elif(cmd == 'list'):
		show_list()
	elif(cmd.isdigit()):
		find_by_id(cmd)
	else:
		find(cmd)



