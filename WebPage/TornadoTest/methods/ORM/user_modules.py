# coding: utf-8

from datetime import datetime
from methods import Base,session
from sqlalchemy import Column, Integer ,String,DateTime,Boolean


class User(Base):
    __tablename__ = "testuser"
    id = Column(Integer,primary_key=True, autoincrement=True)
    username = Column(String(20),nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)
    _locked = Column(Boolean,default=False,nullable=False)

    @classmethod
    def all(cls):
        return  session.query(cls).all()



if __name__ == '__main__':
    Base.metadata.create_all()
