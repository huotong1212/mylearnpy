# def func():
#     fun_lambda_list = []
#     for i in range(4):
#         def lambda_(x):
#             nonlocal i # 不行，这样改每次执行函数的时候还是会向上层作用域索要i，
#                        # 而上层作用域的i已经固定为3了，所有必须写在参数里，让他保存下来，如下
#             a = i
#             print('Lambda函数中 i {} 命名空间为：{}:'.format(a, locals()))
#             return x*i
#         fun_lambda_list.append(lambda_)
#     return fun_lambda_list
#
# fl = func()
# res = []

# res.append(fl[0](1))
# res.append(fl[1](1))
# res.append(fl[2](1))
# res.append(fl[3](1))
#
# print(res)

def func():
    fun_lambda_list = []
    for i in range(4):
        def lambda_(x, i= i):
            print('Lambda函数中 i {} 命名空间为：{}:'.format(i, locals()))
            return x*i
        fun_lambda_list.append(lambda_)
    return fun_lambda_list

fl = func()
res = []

res.append(fl[0](1))
res.append(fl[1](1))
res.append(fl[2](1))
res.append(fl[3](1))

print(res)

# https://www.cnblogs.com/shiqi17/p/9608195.html