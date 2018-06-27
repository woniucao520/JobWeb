#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from handlers.base import BaseHandler

class UserHandler(BaseHandler):
    # 该装饰器的作用，得到当前合法用户
    @tornado.web.authenticated
    def get(self):
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        use_infos  = mrd.select_table(table="users", column="*", condition="username", value=username)
        #this new use_info ((2, 'admin', 'admin'),) 元祖套着元祖模式

        self.render("user.html",users = use_infos)