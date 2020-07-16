def show_list(names):
    for n in names:
        print(f"{n[0]}. {n[1]}")

def find(name, names):
    my_names = [n for n in names if n[1]==name]
    print(my_names)