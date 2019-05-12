
## 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

from student import Teacher,Professor

heart = Teacher()
heart.name = 'SSW'
heart.age = '26'
# heart.score  = 80 #报错 'Teacher' object has no attribute 'score'

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
laodu = Professor()
laodu.score = 99
print(laodu.score)