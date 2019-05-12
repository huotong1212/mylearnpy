
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'grade':
            return 'A'
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

s = Student()
print(s.name)
print(s.age())
print(s.grade)
print(s.score)