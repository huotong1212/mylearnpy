# v = dict.fromkeys(['k1','k2'],[132]) # k1 和 k2都是对应的同一个list对象
# v['k1'].append(666)  # 当k1向该list中添加元素时，k2也会得到反馈
# print(v)
# v['k1'] = 777  # 将k1指向了一个新的对象
# print(v)



def num():
    return[lambda x:i*x for i in range(4)]

print([m(2) for m in num()])

print('\n'.join([' '.join([f'{y} * {x} = {x * y}' for y in range(1, x+1)]) for x in range(1,10)]))

print([i % 2 for i in range(10)])
print((i % 2 for i in range(10))) # ???

print(2==2)
print(1<True)

print(1<2)
print(True==2)