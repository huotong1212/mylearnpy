
import pymysql

# user = input('用户名：>>').strip()
# pwd = input('密码：>>').strip()

# 先连接，拿到游标
conn = pymysql.connect(host='localhost',user='huotong',password='879662581',database='world',charset='utf8')

#拿到游标，即mysql>
cursor = conn.cursor()

#执行sql
# sql = 'select * from country where name like "C%" OR  name like "A%";'
sql = 'select * from country where name like %s OR  name like %s;'
print('sql',sql)

rows = cursor.execute(sql,["C%","A%"])# 拿到受影响的行数
cursor.close()
conn.close()

if rows:
    print('登录成功，rows:',rows)
else:
    print('登录失败')






