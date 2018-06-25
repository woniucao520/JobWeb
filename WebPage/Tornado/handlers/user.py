#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        use_infos  = mrd.select_table(table="users", column="*", condition="username", value=username)
        #this new use_info ((2, 'admin', 'admin'),) 元祖套着元祖模式

        self.render("user.html",users = use_infos)