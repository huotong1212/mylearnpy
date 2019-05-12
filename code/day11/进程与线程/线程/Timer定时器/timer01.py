from threading import Timer


def hello():
    print("hello, world")


t = Timer(1, hello)
t.start()  # after 1 seconds, "hello, world" will be printed