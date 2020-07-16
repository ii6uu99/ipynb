# 掌握5大金刚之string，和9字口诀：基建-增删改查操-切复
# 5大金刚包括: list, tuple, str, set, dict

#1. 基 - 1. 是一个字符序列(sequence)，2. 基于utf-8编码 3. str
#编码：1. ASCII 2. ISO-9995-1 3.ANSI 4.GBK, GB-2312 4.UTF-8
name = '张三'
# print(name)
# for n in 'hellomaishu':
# 	print(n)

# print(dir(str))

#练习：给一个字符串，找出里面所有的o的字符个数

#2. 建 
#2.1 - 简单建 literal
zs = '张三'
ls = "李四"
ww = """王五
fsfds
fsdafdas"""
ww2 = '''王五
fsfds
fsdafdas'''
#2.2 转移字符，引号的互相嵌套
zs = '张\t三'
ls = 'lisi\'s' 
ww = "wangwu's" 

#2.3 构造方法
score = 98.99 
score_str = str(score)
# print(type(score_str))
# print(str([1,2,3]))

#练习：用一个字符串，打印出"静夜思"这首诗

#3. 增: 
#3.1 字符串是immutable 
name = 'zhangsan'
#name[-1] = 'm'
#name2 = 'zhangsan' + 'm'
#3.2 字符串可以被拼接，但任何改变都创建了一个新的字符串
name2 = name[:-1] + 'm'
name3 = name + 'bb'

#3.3 同一个字符串在内存中就只有一份
name4 = name
name5 = 'zhangsan'

# print(id(name))
# print(id(name2))
# print(id(name3))
# print(id(name))
# print(id(name5))

#4. 删 - 不可能的
#5. 改 - 不可能的

#6. 查
#6.1 可以通过下标来访问一个字符
shame = '打工是不可能的！'
#print(shame[-1])

#6.2 子串是否存在 - membership: in, not in 
#identity: is, is not
#print(type(shame) is not str)
# print('可能X' not in shame)

#6.3 开头，结尾
# print(shame.startswith('X打工'))
# print(shame.endswith('！'))

#6.4 下标
# print(shame.index('可能'))

#作业：定义一个字符串的list，里面保存了很多名字，找出所有姓张的人

#7. 操
# 格式化输出
name = 'zhangsan'
greeting = 'hello, ' + name + ', 吃了吗？'
g2 = 'hello, {name}, {name2}, 吃了吗？'
# print(g2.format(name='麦叔', name2='张三'))
# print(f'hello, {name}, 喝了吗？')
# 拆分
names = '张三，李四，王五，二麻子'
# for n in names.split('，'):
# 	print(n)

# 合并
h = 'hello'
names2 = ['张三', '莉莉丝', '王五']
# print(" - ".join(names2))
#print(h.join(name))

# 查找：出现次数, re
name = '我是一个小小小小小小小鸟'
# print(name.count('小'))

# 改变大小写
zhangsan = 'zhangsan is a BAD guy'
# print(zhangsan.title())
# print(zhangsan.capitalize())
# print(zhangsan.upper())
# print(zhangsan.lower())
# print(zhangsan.swapcase())
# print(zhangsan.islower())

# 运算
name8 = ' wangba '
# print(name8 + name)
# print(name8 * 8)

# 去空格
# print(name8.strip())
# print(name8.lstrip())
# print(name8.rstrip())

# 查漏补缺 - 替换
# print(name.replace('小','大'))

#练习: 自行研究dir(str)里面的每个方法的作用

#比较：
print('maishu' > 'Maishu3')
#1个个字符比过去，碰到能决定大小的，就直接返回
#如果一边已经用完了，另一边还有，另一边就赢了
#小写字母大于大写字母；其他顺序查ASCII

#10个字符串练习
#公众号回复：str 

#8. 切片
#9. 复制