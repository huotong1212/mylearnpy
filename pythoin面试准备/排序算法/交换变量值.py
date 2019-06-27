
a = 1
b = 2

# a,b = b,a  # python特有语法，用于数值交换  2 1

a,b = b+2,a  # 4,1

print(a)
print(b)

def fib(max): # 斐波拉契数列 1, 1, 2, 3, 5, 8, 13, 21, 34, ... arr
    n, a, b = 0, 0, 1
    while n < max:
        print(b)          # a=arr[1] b=arr[2]
        a, b = b, a + b   # a=arr[2] b=arr[3]=arr[1]+arr[2]
        n = n + 1
    return 'done'

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a