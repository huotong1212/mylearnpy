
import pymysql

# 先连接，拿到游标
conn = pymysql.connect(host='localhost',user='huotong',password='879662581',database='marvel',charset='utf8')

cursor = conn.cursor()

sql = 'select * from heros;'
rows = cursor.execute(sql)

# 查单条
# res1 = cursor.fetchone()
# res2=cursor.fetchone()
# res3=cursor.fetchone()
# print(res1)
# print(res2)
# print(res3)
# print(res3[0])

# 查多条 fetchmany
# print(cursor.fetchmany(3))
# print(cursor.fetchone())

# 查所有 fetchall
# print(cursor.fetchall())
# print(cursor.fetchone())

# 光标的移动
#1.绝对路径：从文件的开头位置算起
# print(cursor.fetchall())
# cursor.scroll(0,mode='absolute')
# print(cursor.fetchone())
# cursor.scroll(3,mode='absolute')
# print(cursor.fetchone())

#2.相对路径：
print(cursor.fetchone())
print(cursor.fetchone())
cursor.scroll(2,mode='relative') #相对于上面的两条向后移两条
print(cursor.fetchone())

print('%s row in set (0.00 sec)' %rows)
cursor.close()
conn.close()








