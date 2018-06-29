#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        usernames = mrd.select_columns(table="users", column="username")
        one_user = usernames[1][0]
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table = "users", column="*", condition="username",value=username)
        print("select from databases::::",user_infos)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write( username)
            else:
                self.write("you passwod was not right.")
        else:
            self.write("there is no this user.")