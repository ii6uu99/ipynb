from person import Person
class Record():
    def __init__(self, person, action, score):
        self.person = person
        self.action = action 
        self.score = score 

if __name__ == '__main__':
    p = Person(2, '李四')
    r = Record(p, '白嫖', -1)
    print(r.action)