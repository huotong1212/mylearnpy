

### 列表生成器
l1 = []
for x in range(1,10):
    l1.append(x**2)

print(l1)
print([x**2 for x in range(10)])
print([x for x in range(10) if x%2 ==0])
print([m+n for m in 'ABC' for n in 'EFG'])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
l2 = [k + '=' + v for k, v in d.items()]
print(l2)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ x.lower() for x in L1 if isinstance(x,str) ]
print(L2)

