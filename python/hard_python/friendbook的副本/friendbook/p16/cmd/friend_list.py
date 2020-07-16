from friend_data import *
def show_list():
    for n in names:
        print(f"{n[0]}. {n[1]}")

def show_one(person):
    print(f"{person[0]}. {person[1]}")
    show_summary(person[0])
    #show_records(person[0])

def find_by_id(id):
    id = int(id)
    my_names = [n for n in names if n[0] == id]
    if(len(my_names) == 0):
        print(f"无效的ID{id}")
    else:
        person = my_names[0]
        show_one(person)

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

def show_records(id):
    my_records = record_dict[id]
    for r in my_records:
        print(f'{r[0][1]}({r[0][0]}) 给我 {r[1]} {r[3]}')  # 张三(12) 给我 充电 1

def show_summary(id):
    scores = score_dict[id]
    for sid, score in list(scores.items())[-1:-6:-1]:
        print(f"{name_dict[sid]}, {score}")
