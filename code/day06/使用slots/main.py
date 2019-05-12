
from student import Student

ming = Student()

### 动态绑定实例属性
ming.name = 'George'
print(ming.name)

### 动态绑定实例方法
def set_age(self,age):
    self.age = age

from types import MethodType

ming.set_age = MethodType(set_age,ming)  ##给该实例绑定方法
ming.set_age(25)
print(ming.age)

### 但是动态绑定的实例方法对其他实例是不奏效的
jackey = Student()
#jackey.set_age(17)   #报错  'Student' object has no attribute 'set_age'

## 因此，需要给class 绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

### 所有实例均可使用
ming.set_score(60)
jackey.set_score(90)

print(ming.score,'ming')
print(jackey.score,'jackey')