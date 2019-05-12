
class Student(object):
    pass

class Teacher(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称


class Professor(Teacher):
    # 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    pass