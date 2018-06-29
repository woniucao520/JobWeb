#!/usr/bin/env Python
# coding=utf-8

import tornado.web

import json
import pymysql





class UserLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index_1.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="qiwsirtest", port=3306)  # 连接对象

        cur = conn.cursor()
        sql = 'select username from users where username="{}"'.format(username)
        cur.execute(sql)
        data = cur.fetchall()
        if data:
            check_password_sql = 'select * from users  where username="{}" and passwords="{}"'.format(username,password)
            cur.execute(check_password_sql)
            result = cur.fetchall()
            if result:
                success = True
                msg = '验证成功'
            else:
                success = False
                msg = '密码不正确!'
        else:

            success = False
            msg = '无此用户!'
        data = {}
        data['success'] = success
        data['msg'] = msg
        data['data'] = [{'user':username}]
        data['total_num'] = 1
        self.write(json.dumps(data))