from person import *
persons = []
records = [] 

def load_data():
    load_names()
    #load_records()

def load_names():
    with open('names.txt') as name_file:
        lines = name_file.readlines()
        for line in lines:
            id, name = line.split(',')
            persons.append(Person(id, name))

load_data()
print(len(persons))
