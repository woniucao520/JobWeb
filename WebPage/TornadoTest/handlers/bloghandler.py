#!/usr/bin/env Python
# coding=utf-8


import tornado.web
from methods.db import BlogDbApi
import json



class IndexHandler(tornado.web.RequestHandler):
# 首页渲染
    def get(self):
        title = '博客列表'
        blogs_sql = "select * from blog.blog limit 10"
        db = BlogDbApi()
        datas = db._get_data(blogs_sql)
        description = db._get_description(blogs_sql)
        # 如果description 不为空 for循环 遍历 取索引为0的值(也就是字段名) 为空 则调用 _get_fields_meta 方法 取出该表的元数据 字段
        ths = [i[0] for i in description] if description else db._get_fields_meta(schema='blog', table_name='blog')
        print(ths)
        # 将数据集转换为list
        articles = db._get_list_item(ths=ths, datas=datas)
        print(articles)
        self.render('blogindex.html', title=title, articles=articles, ths=ths)

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

class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        blog_id = self.get_argument('blog_id')
        one_blog_sql = 'select * from blog.blog where id={}'.format(blog_id)
        db = BlogDbApi()
        datas = db._get_data(one_blog_sql)
        description = db._get_description(one_blog_sql)
        ths = [i[0] for i in description] if description else db._get_fields_meta(schema='blog', table_name='blog')
        print(ths)
        # 将数据集转换为list
        one_blog = db._get_list_item(ths=ths, datas=datas)
        self.render("test.html",one_blog = one_blog)
