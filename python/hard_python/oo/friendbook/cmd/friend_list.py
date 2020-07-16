from friend_data import *
def show_list():
    for p in persons:
        print(f"{p.id}. {p.name}")

def show_one(person):
    print(f"{person.id}. {person.name}")
    show_summary(person)
    #show_records(person)

def find_by_id(id):
    id = int(id)
    p = find_person(id)
    if(p == None):
        print(f"无效的ID{id}")
    else:
        show_one(p)

def find(name):
    my_persons = [n for n in persons if n.name == name]
    count = len(my_persons)
    if(count == 0):
        print(f"没有:{name}")
    elif(count > 1):
        for n in my_persons:
            print(f"{p.id}. {p.name}")
        print(f"有多个{name}，请输入id选择具体的人")
    else:
        show_one(my_persons[0])

def show_records(person):
    print(person.records)
    for r in person.records:
        # 张三(12) 给我 充电 1
        p2 = r.person
        print(f'{p2.name}({p2.id}) 给我 {r.action} {r.score}')

def show_summary(person):
    for id, score in person.scores.items():
        p = find_person(id)
        print(f"{p.name}, {score}")
