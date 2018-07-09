#!/usr/bin/env Python
# coding=utf-8


import tornado.web
from methods.db import BlogDbApi
import json
import hashlib

class UserLoginHandler(tornado.web.RequestHandler):


    def get(self):
        self.render("login.html")

    def post(self):
        login_email = self.get_argument("login_email")
        login_pwd = self.get_argument("login_pwd")
        # login_pwd = self.md5(login_pwd)
        # 判断注册邮箱是否存在
        checked_email = 'select * from users where email = "{}"'.format(login_email)
        email_info = db.get_data(checked_email)
        if email_info:
            # 判断密码是否正确
            check_pwd = 'select password from users where email = "{}"'.format(login_email)
            pwd_info = db.get_data(check_pwd)
            pwd_info = pwd_info[0][0]


            if login_pwd == pwd_info:
                self.set_secure_cookie("user",login_email)
                data = {'result': 'success', 'msg': "登录成功~~~~"}
                self.write(json.dumps(data))
                self.finish()
            else:
                data = {'result': 'error', 'msg':"密码错误，请您重新输入"}
                self.write(json.dumps(data))
                self.finish()
        else:
            data = {'result': 'error', 'msg': "对不起，该用户不存在"}
            self.write(json.dumps(data))
            self.finish()






