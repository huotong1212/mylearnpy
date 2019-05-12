
import time

class Lazyclassmethod:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        def feedback(*args,**kwargs):
            print('-------描述符Get')
            return self.func(owner)
        return feedback

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    # @staticmethod
    # def now():
    #     t=time.localtime()
    #     return Date(t.tm_year,t.tm_mon,t.tm_mday)

    @classmethod #改成类方法
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday) #哪个类来调用,即用哪个类cls来实例化

    @Lazyclassmethod  # 改成描述符 now = Lazyclassmethod(now)
    def now2(cls):
        t = time.localtime(time.time()+86400)
        return cls(t.tm_year, t.tm_mon, t.tm_mday)  # 哪个类来调用,即用哪个类cls来实例化

class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
print(type(e))

e2=EuroDate.now2()
print(e2) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
print(type(e2))