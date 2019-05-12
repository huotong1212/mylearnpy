
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

### 方法一，将列表生成器的 [],改为()
g = (x for x in range(10))
print(type(g))
print(g.__next__())
print(next(g))
for x in g :
    print(x)

### 方法二，使用yield 关键字
### 这是一个斐波拉契数列（Fibonacci）
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        # print('%s'%(a),end=' ')
        yield a
        n += 1
    return 'Done'

f = fib(10)
print(type(f))

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

for x in fib(10):
    print(x,end=' ')

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

print()
f = fib(6)
while True:
    try:
        next(f)
    except StopIteration as e:
        print('Get Iteration Return Value:',e.value)
        break
