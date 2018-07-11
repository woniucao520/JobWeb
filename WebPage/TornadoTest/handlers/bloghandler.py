#!/usr/bin/env Python
# coding=utf-8


import tornado.web
from methods.db import BlogDbApi
import json
from  markdown import markdown




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

        # 将数据集转换为list
        articles = db._get_list_item(ths=ths, datas=datas)

        # 点击排行
        click_sorted_sql = 'SELECT id,title,views FROM blog.blog ORDER BY views DESC LIMIT 5'
        click_datas = db._get_data(click_sorted_sql)
        click_description = db._get_description(click_sorted_sql)
        click_ths = [i[0] for i in click_description] if click_description else db._get_fields_meta(schema='blog', table_name='blog')
        click_sorted = db._get_list_item(ths=click_ths, datas=click_datas)


        # 最新文章
        latest_sorted_sql = 'SELECT id,title,update_time FROM blog.blog ORDER BY update_time DESC,publish_at  LIMIT 5'
        latest_datas = db._get_data(latest_sorted_sql)
        latest_description = db._get_description(latest_sorted_sql)
        latest_ths = [i[0] for i in latest_description] if latest_description else db._get_fields_meta(schema='blog', table_name='blog')
        latest_sorted = db._get_list_item(ths = latest_ths, datas = latest_datas)


        #博主推荐
        author_recommend_sql = 'SELECT id,title,comments,views FROM blog.blog ORDER BY views DESC, comments  LIMIT 5'
        author_datas = db._get_data(author_recommend_sql)
        author_description = db._get_description(author_recommend_sql)
        author_ths = [i[0] for i in author_description] if author_description else db._get_fields_meta(schema='blog', table_name='blog')
        author_sorted = db._get_list_item(ths = author_ths, datas = author_datas)

        self.render('blogindex.html', title=title, articles=articles,click_sorted=click_sorted, latest_sorted = latest_sorted, author_sorted = author_sorted)



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
        articles = db._get_list_item(ths=ths, datas=datas)

        # 点击排行
        click_sorted_sql = 'SELECT id,title,views FROM blog.blog ORDER BY views DESC LIMIT 5'
        click_datas = db._get_data(click_sorted_sql)
        click_description = db._get_description(click_sorted_sql)
        click_ths = [i[0] for i in click_description] if click_description else db._get_fields_meta(schema='blog',
                                                                                                    table_name='blog')
        click_sorted = db._get_list_item(ths=click_ths, datas=click_datas)

        # 最新文章
        latest_sorted_sql = 'SELECT id,title,update_time FROM blog.blog ORDER BY update_time DESC,publish_at  LIMIT 5'
        latest_datas = db._get_data(latest_sorted_sql)
        latest_description = db._get_description(latest_sorted_sql)
        latest_ths = [i[0] for i in latest_description] if latest_description else db._get_fields_meta(schema='blog',
                                                                                                       table_name='blog')
        latest_sorted = db._get_list_item(ths=latest_ths, datas=latest_datas)

        # 博主推荐
        author_recommend_sql = 'SELECT id,title,comments,views FROM blog.blog ORDER BY views DESC, comments  LIMIT 5'
        author_datas = db._get_data(author_recommend_sql)
        author_description = db._get_description(author_recommend_sql)
        author_ths = [i[0] for i in author_description] if author_description else db._get_fields_meta(schema='blog',
                                                                                                       table_name='blog')
        author_sorted = db._get_list_item(ths=author_ths, datas=author_datas)


        self.render('bloglists.html', title=title, articles=articles, click_sorted=click_sorted, latest_sorted = latest_sorted, author_sorted = author_sorted)






class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        title = "文章详情"
        blog_id = self.get_argument('blog_id')
        one_blog_sql = 'select * from blog.blog where id={}'.format(blog_id)
        db = BlogDbApi()
        datas = db._get_data(one_blog_sql)
        description = db._get_description(one_blog_sql)
        ths = [i[0] for i in description] if description else db._get_fields_meta(schema='blog', table_name='blog')

        # 将数据集转换为list
        one_blog = db._get_list_item(ths=ths, datas=datas)
        blog = one_blog[0]
        blog['content'] = markdown(blog['content'], ['extra', 'codehilite', 'toc',])

        # 点击排行
        click_sorted_sql = 'SELECT id,title,views FROM blog.blog ORDER BY views DESC LIMIT 5'
        click_datas = db._get_data(click_sorted_sql)
        click_description = db._get_description(click_sorted_sql)
        click_ths = [i[0] for i in click_description] if click_description else db._get_fields_meta(schema='blog',
                                                                                                    table_name='blog')
        click_sorted = db._get_list_item(ths=click_ths, datas=click_datas)

        # 最新文章
        latest_sorted_sql = 'SELECT id,title,update_time FROM blog.blog ORDER BY update_time DESC,publish_at  LIMIT 5'
        latest_datas = db._get_data(latest_sorted_sql)
        latest_description = db._get_description(latest_sorted_sql)
        latest_ths = [i[0] for i in latest_description] if latest_description else db._get_fields_meta(schema='blog',
                                                                                                       table_name='blog')
        latest_sorted = db._get_list_item(ths=latest_ths, datas=latest_datas)

        # 博主推荐
        author_recommend_sql = 'SELECT id,title,comments,views FROM blog.blog ORDER BY views DESC, comments  LIMIT 5'
        author_datas = db._get_data(author_recommend_sql)
        author_description = db._get_description(author_recommend_sql)
        author_ths = [i[0] for i in author_description] if author_description else db._get_fields_meta(schema='blog',
                                                                                                       table_name='blog')
        author_sorted = db._get_list_item(ths=author_ths, datas=author_datas)

        self.render("blogdetail.html", blog =blog ,title=title,click_sorted=click_sorted, latest_sorted = latest_sorted, author_sorted = author_sorted)
