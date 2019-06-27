import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://huotong:879662581@127.0.0.1:3306/marvel?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

def task(arg):
    # conn = engine.contextual_connect()
    conn = engine.connect()
    with conn:
        cur = conn.execute(
            "select * from heros"
        )
        result = cur.fetchall()
        print(result)

for i in range(10):
    t = threading.Thread(target = task,args=(i,))
    t.start()
