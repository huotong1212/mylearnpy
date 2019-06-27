#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from db import Users, Hosts

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

session = Session()

# ################ 添加 ################

obj1 = Users(name="wupeiqi")
session.add(obj1)

session.add_all([
    Users(name="wupeiqi"),
    Users(name="alex"),
    Hosts(name="c1.com"),
])
session.commit()


# ################ 删除 ################

session.query(Users).filter(Users.id > 2).delete()
session.commit()

# ################ 修改 ################

session.query(Users).filter(Users.id > 0).update({"name" : "099"})
session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
session.query(Users).filter(Users.id > 0).update({"age": Users.age + 1}, synchronize_session="evaluate")
session.commit()

# ################ 查询 ################

r1 = session.query(Users).all()
r2 = session.query(Users.name.label('xx'), Users.age).all()
r3 = session.query(Users).filter(Users.name == "alex").all()
r4 = session.query(Users).filter_by(name='alex').all()
r5 = session.query(Users).filter_by(name='alex').first()
r6 = session.query(Users).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(Users.id).all()
r7 = session.query(Users).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()



session.close()