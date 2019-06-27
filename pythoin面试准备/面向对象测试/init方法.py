class Person(object):
    def __init__(self):
        print('无参数init')
        pass

    # def __init__(self, name, age, sex):
    #     print('有参数init.....')
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #
    # def eat(self):
    #     print('have lunch')

    def eat(self, food):
        print(f'have {food}')


if __name__ == "__main__":
    p1 = Person()

    # p1.eat()
    p1.eat('hamburger')

### 结论：py不允许重载，后面的同名方法会覆盖原来的
