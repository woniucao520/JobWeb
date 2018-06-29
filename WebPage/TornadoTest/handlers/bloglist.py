#!/usr/bin/env Python
# coding=utf-8

import sys
sys.path.append("..")

import tornado.web
from methods import Base,session
from methods.ORM.user_modules import User





# class BaseHandler(tornado.web.RequestHandler):   # BHandler，可以自定义采用的模板，所有的handler都继承这个类
#
#     @property
#     def session(self):
#         return self.application.session

class BlogList(tornado.web.RequestHandler):

    def get(self):

        session.add_all([User(username='der', password='asdfas'), User(username='sa', password='mima99')])
        session.commit()
        rows = session.query(User).all()
        print("1111",rows)
        self.render('blog_demo.html',rows=rows)


        # query_blogs_sql = 'select * from blog.blog'
        # db = BlogDbApi()
        # datas = db._get_data(query_blogs_sql)
        # description = db._get_description(query_blogs_sql)
        # # 如果description 不为空 for循环 遍历 取索引为0的值(也就是字段名) 为空 则调用 _get_fields_meta 方法 取出该表的元数据 字段
        # ths = [i[0] for i in description] if description else db._get_fields_meta(schema='blog', table_name='blog')
        # print(ths)
        # # 将数据集转换为list
        # blogs = db._get_list_item(ths=ths, datas=datas)
        # print(blogs)
        # self.render('blog_list.html',title=title,blogs=blogs,ths=ths)

