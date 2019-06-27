import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
conn = redis.Redis(connection_pool=pool)

hash = {'a1': 'b1', 'a2': 'b2', 'a3': 3}
conn.hmset('key1', hash)

conn.hset('key2', 't1', 'edg')

print(conn.hget('key1', 'a1'))  # b'b1'
print(conn.hmget('key1', ['a1', 'a2'])) # [b'b1', b'b2']

print(conn.hget('key2', 't1')) # b'edg'
