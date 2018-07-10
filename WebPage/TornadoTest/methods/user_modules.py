# coding: utf-8

from datetime import datetime
from methods import Base,session
from sqlalchemy import Column, Integer ,String,DateTime,Boolean


class User(Base):
    __tablename__ = "testusers"
    id = Column(Integer,primary_key=True, autoincrement=True)
    user_name = Column(String(20),nullable=False)
    password = Column(String(50))
    email = Column(String(50))
    create_time = Column(DateTime)
    is_active = Column(Integer)
    active_token = Column(String(50))
    role_id = Column(Integer)
    update_time = Column(DateTime)




    @classmethod
    def all(cls):
        return  session.query(cls).all()



if __name__ == '__main__':
    Base.metadata.create_all()
