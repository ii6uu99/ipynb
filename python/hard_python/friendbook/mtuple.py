# 掌握5大金刚之tuple，和9字口诀：基建-增删改查操-切复
# 5大金刚包括: list, tuple, set, dict, str

#基本概念: tuple是一个有序的，不可改的数据结构immutable
#l = [5,2,3] #list
t = (5,2,3) #tuple

#优点：1.快 2.安全 3.元组可以被作为dict的key
#python -m timeit '(1,2,3)' #用了9ns左右
#python -m timeit '[1,2,3]' #用了63ns左右
#用的地方：1.参数 2.其他不变的情况

#建
t1 = (5,8,9)
t2 = tuple([1,2,4])
t3 = tuple('maishu')
#t4 = tuple(5) iterable才可以被转换
t5 = (5,)
#print(type(t5))

#print(t1,t2,t3)


#增 - 不能

#删 - 不能

#改 - 不能
a = (1,3,5)
print(id(a))
a = (8,3,5)
print(id(a))

#查
print(a[1])

#操
# a.sort()
# a.reverse()

#切
b = a[0:-1]  #麦叔 大卸八块 sequence
print(b)

#复
c = a[:]
c = a
print(c)

