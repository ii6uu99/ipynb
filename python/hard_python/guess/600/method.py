#局部变量local和全局变量global
#1. 局部变量：def和class内定义的变量
#2. 全局变量：在脚本内（def和class外）定义的变量
#3. 局部变量只有在局部可用
#4. 全局变量可以在global和函数内访问
#5. 局部变量如果和全局变量重名，局部变量优先使用
#6. 全局是指在当前文件（模块）内全局
#7. 在函数内改写全局变量，需要用global关键词
import method2

print(method2.a)

count = 8

def work():
	global count #这个count就是外面那个count
	#count = count + 2
	count = 10
	print(count)

work()
print(count)











