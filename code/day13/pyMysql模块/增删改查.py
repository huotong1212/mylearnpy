
import pymysql

# user = input('用户名：>>').strip()
# pwd = input('密码：>>').strip()

# 先连接，拿到游标
conn = pymysql.connect(host='localhost',user='huotong',password='879662581',database='marvel',charset='utf8')

#拿到游标，即mysql>
cursor = conn.cursor()

#执行sql
# sql = 'select * from country where name like "C%" OR  name like "A%";'
sql = 'INSERT INTO heros(ID,Name,SUPERPOWER) VALUES(%s,%s,%s)'
print('sql',sql)

# rows = cursor.execute(sql,('02','Hulk','genius powerful tough'))# 拿到受影响的行数
rows = cursor.executemany(sql,[('03','Hawkeye','human limitation,archery'),
                               ('04','Black Widow','super spy,beautiful'),
                               ('05','Thor','God power of thunder,high of density')]) # 一次添加多个
conn.commit() #提交到数据库
cursor.close()
conn.close()

if rows:
    print('增加成功，rows:',rows)
else:
    print('增加失败')






