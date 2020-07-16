from person import *
persons = []

def load_data():
    load_names()
    load_records()

def load_names():
    with open('names.txt') as name_file:
        lines = name_file.readlines()
        for line in lines:
            id, name = line.split(',')
            persons.append(Person(id, name))

def load_records():
    with open('records.txt') as file:
        lines = file.readlines()
        for line in lines:
            #3, 于三, 白嫖, 47, 丁九, -1
            points = line.split(',')
            p1 = find_person(points[0].strip())
            p2 = find_person(points[3].strip())
            if(p1 == None or p2 == None):
                continue
            action = points[2].strip()
            score = int(points[5].strip())
            r = Record(p1, action, score)
            p2.add_record(r)

def find_person(id):
    ps = [p for p in persons if p.id == id]
    if(len(ps)>0):
        #print(f'found {ps[0].name}')
        return ps[0]
    
load_data()
for p in persons:
    print(f'{p.name} has {len(p.records)} records')
