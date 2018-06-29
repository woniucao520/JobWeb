# coding=utf-8


from handlers.index import *
from handlers.user import UserHandler
from handlers.handlers import *
from  handlers.bloglist import *

url = [

    (r'/user/login',UserLoginHandler),
    (r'/blog/list',BlogListHandler),
    (r'/blog/demo',BlogList)
]