
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，
# 用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

def createCounter():
    i = 0
    def counter():
        nonlocal i  #使用外层变量
        i+=1
        return i
    return counter

def createCounter1():
    li = [0]
    def counter():
        li.append(li[-1] + 1)
        return li[-1]
    return counter

countA = createCounter()
print(countA(),countA())

# countB所指向的仅仅是counter这个函数,只是可以调用createCounter1中的局部变量
countB = createCounter1()
print(countB(),countB())
