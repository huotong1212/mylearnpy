
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):  # 返回用户看到的字符串
        return 'Student Name is %s' %(self.name)

    __repr__ = __str__ # 返回程序开发者看到的字符串

print(Student('Michel'))
s = Student('Duck')
print(s)
