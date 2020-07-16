# 掌握5大金刚之dict，和9字口诀：基建-增删改查操-切复
# 5大金刚包括: list, tuple, str, set/frozenset, dict

#1.基础 - 键值对，key:value, key必须是immutable的对象
s = {'zs':66, 'lis':88, 'ms':100}
s = {'zs':{'dd':88, 'xx':99}, 'lis':88, 'ms':100}

#2.创建
s = {'zs':66, 'lis':88, 'ms':100} #set也用大括号，直接{}是创建一个空的字典，而不是set
s = dict() #一个空的字典
s = dict([(1,99), (2,88), (3,100)]) #包含成对的数据的iterable
print(s)

names = ['za', 'lis', 'ww', 'wb']
scores = [78, 56, 78, 99]
s = dict(zip(names, scores)) #zip是拉链的意思
print(s)

s3 = dict.fromkeys(names, 19)
print(s3)


#3.增
s['ruhua'] = 89
print(s)
s['damei'] = 77
print(s)

#4.删 del pop, popitem, clear
#del s['damei'] #如果删除的key不存在，会抛出KeyError
# print(s)
# print(s.pop('ruhua'))
# print(s)
# print(s.popitem())
# print(s)
# s.clear()
# print(s)

#5.改 
print(s)
s['damei'] = 99
print(s)

#6.查 [], get, in, not in
print('ww' in s) 
print(s['ww'])
print(s.get('wwx'))
print(s)
s.setdefault('www', 'google.com')
print(s['www'])

#7.操 遍历，items, keys, values, sort
for k in s:
	print(k, s[k])
print(list(s.keys()))
print(list(s.values()))
print(list(s.items()))

s2 = {k:v for k,v in sorted(s.items())}
print(s2)
# Python小技巧#7：如何给字典Dict按照Value排序？

#8.切片 fromkeys
#9.复制 copy
s4 = s.copy()
print(s4)
s5 = {'dfd':88, 'xxx':89, 'ww':120}
print(s)
print(s5)
s.update(s5)
print(s)

