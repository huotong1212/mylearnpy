from twisted.internet import reactor   # 事件循环（终止条件，所有的socket都已经移除）
from twisted.web.client import getPage # socket对象（如果下载完成，自动从时间循环中移除...）
from twisted.internet import defer     # defer.Deferred 特殊的socket对象 （不会发请求，手动移除）

_close = None
count = 0


def response(content):
    print(content)
    global count
    count += 1
    # if count == 3:
    #     _close.callback(None)

def all_request():
    print('1111111')
    # 每个爬虫的开始：stats_request
    url = "http://www.baidu.com"
    d1 = getPage(url.encode('utf-8'))
    d1.addCallback(response)

    url = "http://www.cnblogs.com"
    d2 = getPage(url.encode('utf-8'))
    d2.addCallback(response)

    url = "http://www.bing.com"
    d3 = getPage(url.encode('utf-8'))
    d3.addCallback(response)

@defer.inlineCallbacks
def task():
    reactor.callLater(0, all_request)

    global _close
    _close = defer.Deferred()
    yield _close


def done(*args, **kwargs):
    reactor.stop()


# 每一个爬虫
spider1 = task()
# spderd2 = task()
dd = defer.DeferredList([spider1])
dd.addBoth(done)

reactor.run()