import random
import time
import memory_profiler as mem


names = ['zhangsan', 'lisi', 'wangwu', 'maishu', 'xiaomai']
city = ['hangzhou', 'beijing', 'shanghai', 'guangzhou', 'shenzhen']


def generate(nums):
    for i in range(nums):
        person = {
            'name': random.choice(names),
            'age': random.choice(city),
            'desc': 'hello, how are you, my name is maishu, i love you truly. Winter is coming. Crono is coming',
            'id': i
        }
        yield person


def build(nums):
    result = []
    for i in range(nums):
        person = {
            'name': random.choice(names),
            'age': random.choice(city),
            'id': i
        }
        result.append(person)
    return result


print(time.time())
print(f'memory before: {mem.memory_usage()}')
#generate(1000000)
build(3000000)
print(f'memory after: {mem.memory_usage()}')
print(time.time())
