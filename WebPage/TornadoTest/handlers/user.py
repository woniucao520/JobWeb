# coding = utf-8

import tornado.web
import methods.readdb as mrd

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        print("news User_infos",user_infos)
        self.render("user.html",users = user_infos)