
import time
import os

print(time.time())
print(time.ctime())
print(time.clock())
print(time.gmtime()) #格林尼治时间
print(time.localtime()) #当前时区时间

print(time.timezone/3600)


# ZONES = ["GMT", "EUROPE/Amsterdam"]
# for zone in ZONES:
#       os.environ["TZ"] = zone #os.environ['环境变量名称']='环境变量值' 其中key和value均为string类型
#       time.tzset()

now = time.ctime()
t = time.strptime(now)
print(t)


from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print(s)

from time import mktime, gmtime
t = mktime(gmtime())
print(t)