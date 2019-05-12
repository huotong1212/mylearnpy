import pymysql

# 获取插入的最后一条数据的自增ID
# 先连接，拿到游标
conn = pymysql.connect(host='localhost',user='huotong',password='879662581',database='marvel',charset='utf8')

cursor = conn.cursor()

sql = 'INSERT INTO heros(Name,SUPERPOWER) VALUES(%s,%s)'
print('sql',sql)

rows = cursor.execute(sql,('Scarlet Witch','chaotic magic'))

conn.commit()
print(cursor.lastrowid) # 查看表中最后一行的ID,必须是自增长的才能看见

cursor.close()
conn.close()




