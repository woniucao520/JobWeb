#!/usr/bin/env Python
# coding=utf-8


import tornado.web
from methods.db import BlogDbApi
import json

class UserLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")