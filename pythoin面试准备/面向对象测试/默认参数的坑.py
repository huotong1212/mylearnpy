# 正常没毛病的操作
def func(a,b=False):
    print(a)
    print(b)
func(1,True)  # 在实参角度,传的的True对默认关键字参数进行了修改操作
# 结果
1
True

# 坑来了
# 就是当你的默认参数如果是可变的数据类型，你要小心了
# 也就是 def func(a,b=[1,2,3,4])这个时候要小心b列表中的内容
def func(a,li=[]):
    li.append(a)
    return li
print(func(1)) # 输出结果 [1]
print(func(2)) # 输出结果 [1,2]
print(func(3)) # 输出结果 [1,2,3]

# 总结
# 就是列表中的内容会一直增加,不会被替换,结果 [1,2,3] l = []中的内容不会随着函数的结束而消失