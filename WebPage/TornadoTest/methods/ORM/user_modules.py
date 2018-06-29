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

    # 自己封装查询方法
    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_id(cls,id):
        return session.query(cls).filter_by(id=id).all()

    @classmethod
    def get_username(cls,username):
        return session.query(cls).filter_by(username=username).all()

    @property
    def locked(self):
        return self._locked

    def __repr__(self):
        return "<User(id='%s',username='%s',password='%s',creatime='%s',_locked='%s')>"%(
            self.id,
            self.username,
            self.password,
            self.creatime,
            self._locked
        )



if __name__ == '__main__':
    Base.metadata.create_all()
