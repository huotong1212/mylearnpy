import threading


class SingleTon(object):
    instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SingleTon.instance_lock:
                # 这里不适用__instace命名的原因是
                # 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
                # 所以，仍然可以通过_Student__name来访问__name变量
                if not hasattr(cls, '_instance'):
                    # 添加一个类属性_instance，实例为父类的实例
                    SingleTon._instance = super().__new__(cls, *args, **kwargs)
                    # SingleTon._instance = object.__new__(cls)
        return SingleTon._instance


if __name__ == '__main__':
    s1 = SingleTon()
    s2 = SingleTon()

    print(s1 == s2)
    print(s1 is s2)


    def task(i):
        a = 1 + i
        s = SingleTon()
        print(s)


    t1 = threading.Thread(target=task, args=[1, ])
    t2 = threading.Thread(target=task, args=[2, ])

    t1.start()
    t2.start()
