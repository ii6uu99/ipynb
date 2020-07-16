class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.records = []
        self.scores = {}
    
    def add_record(self, record):
        self.records.append(record)
        self.scores.setdefault(record.person.id, 0)
        self.scores[record.person.id] = self.scores[record.person.id] + record.score 

    def remove_record(self, record):
        self.records.remove(record)

class Record():
    def __init__(self, person, action, score):
        self.person = person
        self.action = action
        self.score = score

if __name__ == '__main__':
    p1 = Person(1, '张三')
    p2 = Person(2, '李四')
    r = Record(p2, '暴打', -5)
    p1.add_record(r)
    assert len(p1.records) == 1, '应该有1条record'
    p1.remove_record(r)
    assert len(p1.records) == 0, '应该有0条record'
