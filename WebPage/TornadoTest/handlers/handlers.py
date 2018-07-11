#!/usr/bin/env Python
# coding=utf-8

import tornado.web
from methods.db import BlogDbApi
import json






class UserLoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index_1.html",title='title')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        db = BlogDbApi()
        sql = 'select username from users where username="{}"'.format(username)
        data = db._get_data(sql)
        if data:
            check_password_sql = 'select * from users  where username="{}" and passwords="{}"'.format(username,password)
            result = db._get_data(check_password_sql)
            if result:
                success = True
                msg = '验证成功'
            else:
                success = False
                msg = '密码不正确!'
        else:

            success = False
            msg = '无此用户!'
        data = {}
        data['success'] = success
        data['msg'] = msg
        data['data'] = [{'user':username}]
        data['total_num'] = 1
        self.write(json.dumps(data))

class BlogListHandler(tornado.web.RequestHandler):
    def get(self):
        title = '博客列表'
        query_blogs_sql = 'select * from blog.blog'
        db = BlogDbApi()
        datas = db._get_data(query_blogs_sql)
        description = db._get_description(query_blogs_sql)
        # 如果description 不为空 for循环 遍历 取索引为0的值(也就是字段名) 为空 则调用 _get_fields_meta 方法 取出该表的元数据 字段
        ths = [i[0] for i in description] if description else db._get_fields_meta(schema='blog', table_name='blog')

        # 将数据集转换为list
        blogs = db._get_list_item(ths=ths, datas=datas)

        self.render('blog_list.html',title=title,blogs=blogs,ths=ths)

