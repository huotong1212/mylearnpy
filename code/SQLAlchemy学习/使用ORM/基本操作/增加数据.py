from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from SQLAlchemy学习.使用ORM.创建数据表.signleTable import User

engine = create_engine("mysql+pymysql://huotong:879662581@127.0.0.1:3306/marvel", max_overflow=0, pool_size=5)
##############方式一########################
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
session = Session()

# ############# 执行ORM操作 #############
obj1 = User(username="alex1",password='123456')
session.add(obj1)

# 提交事务
session.commit()
# 关闭session
session.close()

######################方式二####################