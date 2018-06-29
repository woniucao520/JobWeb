# encoding: utf-8

# 引入基本包

from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 连接数据库数据

HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "blog"
USERNAME = "root"
PASSWORD = "123456"


# DB_URL的格式
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

# 创建引擎
engine = create_engine(DB_URI, echo = False)

Base = declarative_base(engine)
# sessionmaker 生成一个session类

Session = sessionmaker(bind=engine)
session = Session()