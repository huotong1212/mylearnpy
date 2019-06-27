import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
conn = redis.Redis(connection_pool=pool)

# 保存顺序为: 3,2,1
conn.lpush('oo', 1, 2, 3)

# 返回个数
print(conn.llen('oo'))  # 3
print(conn.lrange('oo', 0, -1))  # [b'3', b'2', b'1']
# 在name对应的列表的某一个值前或后插入一个新值
conn.linsert('oo', 'AFTER', 2, 'alex')

# 对name对应的list中的某一个索引位置重新赋值

'''
# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
    # 1、获取name对应的所有列表
    # 2、循环列表
# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：
 
def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
 
# 使用
for item in list_iter('pp'):
    print item
'''
