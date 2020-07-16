# 掌握5大金刚之set，和9字口诀：基建-增删改查操-切复
# 5大金刚包括: list, tuple, str, set/frozenset, dict

#1. 基础：不能重复，不分先后，只能加入immutable(不可变)的内容
class Person:
	def __init__(self, name):
		self.name = name
p = Person('wangwu')

names = {'zs', 'lisi', 'zs', p}
# print(names)
# p.name = 'wangwuwu'
# print(names)
#什么情况下用set

#2. 创建: 大括号，空的代表dict，用set可以空的，也可以转换iterable的对象
score = set()
score = {98,89,69,96}
score = set((4,5,6)) #iterable
#print(score)

#3. 增
score.add('zs')
#print(score)

#4. 删
score.remove('zs')
#print(score)
score.discard('ls') #有就移除，没有就什么也不错，但不会报错
#print(score)
score.clear() #清楚所有内容
#print(score)

#5. 改 - 没有顺序
#6. 查 in not in 成员运算符
score = {98,89,69,96}
#print(98 not in score)
print(score.pop())
for i in score:
	print(i)

#7. 操作：set集合 - 并，交
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
#合并
s3 = s1 | s2
s3 = s1.union(s2)
#交
s3 = s1 & s2 #s1.intersection(s2)

#差
s3 = s1 - s2

#不重复的集合
s3 = s1 ^ s2

#比较
print(s1.issuperset(s2)) #s1 > s2
print(s3)

#8.切片
#9.复制
p2 = Person('lisi')
score.add(p2)
print(score)
s4 = score.copy()
print(s4)

#10. frozenset
s5 = frozenset(s4)
print(s5)
s5.add(88)



