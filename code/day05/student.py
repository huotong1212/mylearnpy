
## 演示封装

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        self.grade = 6

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        if score<0:
            return 'score must more than 0'
        elif score>100:
            return 'score must less than 100'
        else:
            self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        if self.__score < 60:
            return 'D'
        elif self.__score < 80:
            return 'C'
        elif self.__score < 90:
            return 'B'
        else:
            return 'A'