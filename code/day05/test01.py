
from student import Student

s = Student('tony',20)
# print(hasattr(s,'grade')) #True
# print(hasattr(s,'set_name')) #True

# if hasattr(s,'grade'):
#     setattr(s,'grade',6)
#     print(getattr(s,'grade')) # 6
#     print(getattr(s,'age',15)) # 15 若对象中没有该属性，则15为默认值
# if hasattr(s,'set_name'):
#     setname = getattr(s,'set_name')
#     setname('Stack')
#     getname = getattr(s,'get_name')
#     print(getname()) # Stack

delattr(s,'grade')
print(s.grade)