from friend_data import *
def show_list():
    for n in names:
        print(f"{n[0]}. {n[1]}")

def show_one(person):
    print(f"{person.id}. {person.name}")
    #show_summary(person[0])
    show_records(person)

def find_by_id(id):
    id = int(id)
    p = find_person(id)
    if(p == None):
        print(f"无效的ID{id}")
    else:
        show_one(p)

def find(name):
    my_names = [n for n in names if n[1]==name]
    count = len(my_names)
    if(count == 0):
        print(f"没有:{name}")
    elif(count > 1):
        for n in my_names:
            print(f"{n[0]}. {n[1]}")
        print(f"有多个{name}，请输入id选择具体的人")
    else:
        show_one(my_names[0])

def show_records(person):
    print(person.records)
    for r in person.records:
        # 张三(12) 给我 充电 1
        p2 = r.person
        print(f'{p2.name}({p2.id}) 给我 {r.action} {r.score}')

def show_summary(id):
    scores = score_dict[id]
    for sid, score in list(scores.items())[-1:-6:-1]:
        print(f"{name_dict[sid]}, {score}")
