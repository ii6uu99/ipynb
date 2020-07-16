#569实现自己的可循环类-随机数循环
import random 
class RandomCount:
	def __iter__(self):
		return self 
	def __next__(self):
		r=random.randint(1，10)
		if(r==9):
			raise StopIteration 
		return r 
rc=RandomCount()
for s in rc:
	print(s)