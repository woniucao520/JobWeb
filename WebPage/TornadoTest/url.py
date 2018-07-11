# coding=utf-8


from handlers.bloghandler import IndexHandler

from handlers.handlers import *

from handlers.userhandler import *
from handlers.bloghandler import *


url = [

    (r'/user/login',UserLoginHandler),


    (r'/index',IndexHandler),
    # (r'/article/list',ArticleListHandler)
    (r'/blog/detail',DetailHandler),
    (r'/blog/article',BlogListHandler),

    (r'/user/login',UserLoginHandler),
    (r'/user/registered',UserRegisteredHandler),

]




