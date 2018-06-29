# coding=utf-8

from methods import  engine
from  methods.ORM.user_modules import Base

def run():
    Base.metadata.create_all(engine)