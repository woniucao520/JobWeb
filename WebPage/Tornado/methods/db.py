#coding=utf-8

import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="qiwsirtest", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象
