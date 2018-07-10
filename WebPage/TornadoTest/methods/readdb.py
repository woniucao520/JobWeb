# #!/usr/bin/env Python
# # coding=utf-8
#
# # import sys
# # sys.path.append("..")
#
# from methods.db1 import *
#
# def select_table(table, column, condition, value ):
#     sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
#     cur.execute(sql)
#     lines = cur.fetchall()
#     return lines
#
#
# def select_columns(table, column ):
#     sql = "select " + column + " from " + table
#     cur.execute(sql)
#     lines = cur.fetchall()
#     return lines