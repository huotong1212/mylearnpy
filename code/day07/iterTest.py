
class Too(object):
    def __init__(self):
        self.no = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.no += 1
        if self.no > 10:
            raise StopIteration('no > 10, stop')
        return self.no

t = Too()
for x in t:
    print(x)
