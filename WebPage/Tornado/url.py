# coding=utf-8



from handlers.index import IndexHandler
from  handlers.user import UserHandler
from handlers.sleep import SeeHandler,SleepHandler


url = [
    (r"/", IndexHandler),
    (r"/user",UserHandler),
    (r"/see",SeeHandler),
    (r"/sleep",SleepHandler)
]