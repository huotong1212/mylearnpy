import redis

pool = redis.ConnectionPool(host='localhost',port=6379)
conn = redis.Redis(connection_pool=pool)

#添加 同名则修改
conn.set('a',1)

# 批量添加
# conn.mset(k1="v1",k2="v2")
conn.mset({'k3':5,'k4':6})

# 批量获取
result = conn.mget({'k1','k2'}) # [None, None]
print(result)
result = conn.mget('k3','k4') # [b'5', b'6']
print(result)

# 设置新值并获取原来的值
r = conn.getset('a','abc')

print(conn.get('a')) # b'abc'