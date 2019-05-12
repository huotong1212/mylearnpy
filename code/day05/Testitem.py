
class Boo:
    def __init__(self):
        self.name = 'Jack'
        self.age = 60
        self.grade = 10

    def __getitem__(self, item):
        return 234

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        return 'set_item'

    def __delitem__(self, key):
        print(key)
        # delattr(self, 'grade')
        del self.__dict__[key]

b = Boo()
print(b[1])  # 执行了getitem 234
b['grade'] = 12
print(b.grade) # 执行了setitem grade = 12
del b['grade']  # 执行了delitem 删除grade
print(b.grade)

