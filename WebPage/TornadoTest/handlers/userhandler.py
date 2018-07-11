#!/usr/bin/env Python
# coding=utf-8


import tornado.web
from methods.db import BlogDbApi
import json
from datetime import datetime
import hashlib


from methods import session
from methods.user_modules import User




class UserLoginHandler(tornado.web.RequestHandler):

    def md5(self,param):
        m = hashlib.md5()
        m.update(param.encode('utf8'))
        return m.hexdigest()


    def get(self):

        self.render("login.html")

    def post(self):
        login_email = self.get_argument("login_email")
        login_pwd = self.get_argument("login_pwd")
        db = BlogDbApi()
        login_pwd = self.md5(login_pwd)
        # login_pwd = self.md5(login_pwd)
        # 判断注册邮箱是否存在
        checked_email = 'select * from testusers where email = "{}"'.format(login_email)
        email_info = db._get_data(checked_email)
        if email_info:
            # 判断密码是否正确
            check_pwd = 'select password from testusers where email = "{}"'.format(login_email)
            pwd_info = db._get_data(check_pwd)
            pwd_info = pwd_info[0][0]

            if login_pwd == pwd_info:
                self.set_secure_cookie("user",login_email)
                data = {'result': 'success', 'msg': "登录成功~~~~"}
                self.write(json.dumps(data))
                self.finish()
            if login_pwd != pwd_info and len(login_pwd)>0:

                data = {'result': 'error', 'msg':"密码错误，请您重新输入"}
                self.write(json.dumps(data))
                self.finish()

        if not email_info and  len(login_email)>0:
            data = {'result': 'error', 'msg': "对不起，该用户不存在"}
            self.write(json.dumps(data))
            self.finish()

# 注册
class UserRegisteredHandler(tornado.web.RequestHandler):


    def md5(self,param):
        m = hashlib.md5()
        m.update(param.encode('utf8'))
        return m.hexdigest()

    def get(self):
        self.render("login.html")

    def post(self):
        register_username = self.get_argument("register_username")
        register_pwd = self.get_argument("register_pwd")
        register_pwd = self.md5(register_pwd)
        register_email = self.get_argument("register_email")
        check_username_sql = 'select * from users where user_name ="{}"'.format(register_username)
        check_email_sql = 'select * from users where email = "{}"'.format(register_email)
        db = BlogDbApi()
        register_username_info = db._get_data(check_username_sql)
        register_email_info = db._get_data(check_email_sql)
        if register_username_info:
            data = {'result':'error','msg':"用户名已经被占用"}
            self.write(json.dumps(data))
            self.finish()

        if register_email_info:
            data = {'result': 'error', 'msg': "邮箱已经存在"}
            self.write(json.dumps(data))
            self.finish()
        create_time = datetime.now()
        is_active = 1
        active_token = "abc"
        role_id = 3
        # 插入数据库操作
        # insert_sql = 'insert into users(user_name,password,email,create_time,is_active,active_token,role_id) values (%s,%s,%s,%s,%s,%s,%s)'
        testusers = User()
        testusers.user_name = register_username
        testusers.password = register_pwd
        testusers.email = register_email
        testusers.create_time = create_time
        testusers.is_active = is_active
        testusers.active_token = active_token
        testusers.role_id = role_id

        session.add(testusers)
        session.commit()

        data = {'result': 'success', 'msg': "恭喜，注册成功"}
        self.write(json.dumps(data))



        session.close()


















