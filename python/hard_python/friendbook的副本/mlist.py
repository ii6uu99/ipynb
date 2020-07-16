# 掌握5大金刚，和8字口诀：建-增删改查操-切复

# 1. 5大金刚和各自的特点
# 作业: 1. 写出5大金刚各自的特点 2.记住8字口诀 3.整理知识导图
# 2. immutable和mutable
# score = 99
# s2 = score
# print("old score: ", id(score))
# print("old s2: ", id(s2))

# score = 98
# print("new score: ", id(score))
# print("new s2: ", id(s2))

# name = 'maishu'
# name += ' is dog'
# print(name)
# #name[2] = 'x'
# print(name[2])

# t1 = (1,2,3)
# t1 = (2, 3, 4)
# #t1[0] = 5

# ===8种玩法========
# A: 创建 - [], list(), range()
#建1
# names = ['zhangsan', 'lisi', 'wangwu']
# empty_names = []
# print(names)
# #建2
# names = list() #创建1个空的列表
# #可以接受一个iterable的对象
# names = list(range(8)) 
# names = list((1,2,3,4))
# names = list('maishu is bad')
# from collections.abc import Iterable
# print(isinstance(345, Iterable))
# print(names)
#有序ordered vs 排序sorted：先来后到的自然顺序；一个是按照某种要求排列

# B: 增添加元素: append, insert, extend, +
names = []
#增1
names.append('maishu')
names.append('表叔')
names.append('麦二叔')
names.append(3)
#names.append((3,4,5))
#增2
names.insert(3, 886)

#增3 - 插入的下标超出了长度，就放在最后
names.insert(-3, 886)

#增4 
bad_guys = ['麦叔', '小麦']
#names.append(bad_guys)
names.extend(bad_guys)
#names += bad_guys
#print(names)

# C: 删除元素的3种方法: del, pop, remove
#两种删除方法：根据下标，根据内容删除
#删1: del
# print(names)
# del names[2]
# print(names)

#删2：pop 
# - 默认去掉最后一个
# - 可以指定下标
# - 会返回pop的值
# - 如果下标越界，抛出IndexError
# names.pop()
# n = names.pop(1)
# names.pop(13)
# print(n)
# if(len(names)>index): #可以先判断
# print(names)

#删3：
# - 只会删除第一个符合条件的
# - 如果没有符合条件的，就抛出ValueError
# print(names)
# names.remove('maishu')
# print(names)
#names.remove('maishu') #会抛出ValueError
# if 'maishu' in names:
#     names.remove('maishu')

# 改：修改元素的值
#改1
# print(names)
# names[1] = 'biaoshu'
# #改2
# print(names)
# names[10] = 'biaoshu'
#改3 - list里面保存的是实际对象的地址，修改的过程就是指向了新的地址

# 查：查询元素[], index(), len()
#查1：下标从0开始，也可以从-1开始
#查2: 下标越界，会出现IndexError
# print(names)
# print(names[0])
# print(names[-1])
#print(names[9])
#查3:index查询下标，如果没有，会抛出ValueError
# print(names.index(886))
#print(names.index(8866))
#查4：in, not in 
# if(8866 not in names):
#     names.append(8866)
# else:
#     names.index(8866)
#查4:len()
# print(len(names))

# 操做：loop,  +, *, ==, sort, reverse, max, min, sum
# 操1：loop
# for n in names:
#     print('hello, ', n)

# for index, n in enumerate(names):
#     print(f'no {index + 1} is {n}')

# 操2：基本运算
scores = [87, 65, 98, 32]
scores2 = [87, 65, 98, 33]
# print(names + scores) #extend是一样的效果
# print(scores * 3)
# print(scores == scores2)

#操3: 排序 ordered sorted
# list.reverse() 会修改原列表
# reversed(list) 不会修改原列表，会返回一个新的
# sort同上
# sort可以指定reverse=True
# sort可以指定key
# print(scores)
# print(sorted(scores, reverse=True))
# scores.reverse()
# print(scores)
# scores.sort()
# print(scores)
# scores.sort(reverse=True)
# print(scores)

# name_scores = [('zhangsan', 87), ('maishu', 100), ('lisi', 98)]
# print(sorted(name_scores, key=lambda n: n[1]))
#字符串的比较，是1个个字符比较过去，按照字符顺序，
#如果前面都一样，长的那个算大 maishu maishub

#操4：max, min, sum
# print(max(scores))
# print(min(scores))
# print(sum(scores))
# names = ['zhangsan', 'lisi', 'maishu']
# print(names)
# print(max(names))
# print(min(names))
#print(sum(names))

# 切片操作 start:end:step
# print(names)
# print(names[1:6:2])
#其他请参考：https://www.bilibili.com/video/BV137411W7Xo

# 复：推导式Comprehension，map, filter
# print(names)
# names2 = names[:]
# print(id(names))
# print(id(names2))
nums = list(range(100))
# print(nums)

# sq_nums = [n*n for n in nums]
# print(sq_nums)
nums_3 = [n+8 for n in nums if n%3==0]
print(nums_3)

print(list(map(lambda n: n*8, nums)))
