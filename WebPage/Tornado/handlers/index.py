#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("index.html",user = one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_current_cookie(username)
                self.write(username)
            else:
                self.write("your password was not right.")
        else:
            self.write("there is no this user")

# 增加了一个方法 set_current_user() 用于将用户名写入 cookie
    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):
    def get(self):
        self.render("error.html")