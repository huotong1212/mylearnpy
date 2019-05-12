
class Student(object):

    @property  #把一个getter方法变成属性
    def score(self):
        return self.__score

    @score.setter
    def score(self, value): #此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    #还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    #下面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth



s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()