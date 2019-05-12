
from student import Student

# bart = Student()
# bart.name = 'Simon'
# print(bart.name)

# bart = Student('Simon',59)
# print(bart.get_name(),bart.get_score())

from animal import *

a = Animal()
husky = Dog()
gaffey = Cat()

### 使用type判断对象类型
print(type(123))
print(type(a))
print(type(max))
print(type(123) == int) #type的返回值为对应的class类型

print('-'*20)
### 使用instance判断class的类型
print(isinstance(husky,Dog))
print(isinstance(husky,Animal))
print(isinstance(a,Dog))

print('---------------')
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance(123,int))

###使用dir获取一个对象的属性和方法
print('-'*20)
print(dir('abc'))
print(dir(husky))

### 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
print(hasattr(husky,'name'))
setattr(husky,'age',6)
print(getattr(husky,'age'))
print(getattr(husky,'name','jeff'))
print(hasattr(husky,'run'))
print(getattr(husky,'run'))
