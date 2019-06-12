class Property:
    def __init__(self, fget):
        self.fget = fget    # 为实例增加方法，这里的方法是未绑定实例的，不会自动传入实例self
        self.fset = None    # 同上，未绑定实例

    def __get__(self, instance, owner):
        if instance is not None:
            return self.fget(instance)  # 调用原方法，传入实例self
        return self

    def __set__(self, instance, value):
        self.fset(instance, value)  # 调用原方法，传入实例self和value

    def setter(self, func):
        self.fset = func  # 更新属性
        return self

class A:
    def __init__(self, data):
        self._data = data

    @Property  # data = Property(data) 描述符实例
    def data(self):
        return self._data

    @data.setter  # data = data.setter(data) 更新属性，并返回描述符实例
    def data(self, value):
        self._data = value