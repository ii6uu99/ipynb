from friend_data import *
def show_list():
    for n in names:
        print(f"{n[0]}. {n[1]}")


def show_one(person):
    print(f"{person[0]}. {person[1]}")

def find(name):
    my_names = [n for n in names if n[1]==name]
    count = len(my_names)
    if(count == 0):
        print(f"没有:{name}")
    elif(count > 1):
        for n in my_names:
            show_one(n)
    else:
        show_one(my_names[0])
