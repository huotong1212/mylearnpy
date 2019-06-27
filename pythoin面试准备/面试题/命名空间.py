def func():
    fun_lambda_list = []
    for i in range(4):

        def lambda_(x):
            print('Lambda函数中 i {} 命名空间为：{}:'.format(i, locals()))
            return x*i
        fun_lambda_list.append(lambda_)
        print('外层函数 I 为：{} 命名空间为:{}'.format(i, locals()))

    return fun_lambda_list

fl = func()
fl[0](1)
fl[1](1)
fl[2](1)
fl[3](1)