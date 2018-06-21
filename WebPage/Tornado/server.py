# coding = utf-8
# 目的是将程序运行起来

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application

from tornado.options import define, options

define("port", default = 8000, help = "run on the given port, type = int" )

def main():
    tornado.options.parse_command_line();

