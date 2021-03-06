# #coding:utf-8
#
# import pymysql
#
# class BlogDbApi():
#     def __init__(self):
#         self.conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="blog", port=3306,charset='utf8')  # 连接对象
#         self.cur = self.conn.cursor()
#
#     def _get_data(self,sql):
#         """
#         返回数据集对象
#         :param sql: 原生sql语句
#         :return:
#         """
#         self.cur.execute(sql)
#         data = self.cur.fetchall()
#         return data
#
#     def _get_description(self,sql):
#         """
#         执行sql后的描述
#         :param sql:
#         :return:
#         """
#         self.cur.execute(sql)
#         return self.cur.description
#
#     #获取数据库的字段
#     def _get_fields_meta(self, schema,table_name):
#         """
#         返回某个数据库下某个表的字段列表
#         :param schema: 数据库名称
#         :param table_name: 数据表名称
#         :return:
#         """
#         base_sql = r'''
# select COLUMN_NAME as column_name
# From information_schema.COLUMNS
# where TABLE_SCHEMA = '{}' and  TABLE_NAME = '{}'
# '''
#         sql = base_sql.format(schema,table_name)
#
#         results = self._get_data(sql)
#         fields = [i[0] for i in results]
#         return fields
#     #将数据库数据 转为list list里为字段{'字段1':字段1值,}
#
#     def _get_list_item(self,ths,datas):
#         """
#
#         :param ths: 数据库字段列表
#         :param datas: 数据集对象
#         :return:
#         """
#         items_list = []
#         for data in datas:
#             item = dict(zip(ths,data))
#             items_list.append(item)
#         return items_list
#
#     def _update(self,table, updates_condition, where_condition):
#         """
#
#         :param table: 数据表
#         :param updates: 更新条件字典 {'title':'test1'}
#         :param where_condition: where 条件字典 {'id':'4'} 或者为空
#         :return:
#         """
#         base_sql = "update  {table} set {updates} {where}"
#         update_lst = [k + '="' + v + '"' for k, v in updates_condition.items()]
#         updates = ','.join(update_lst).rstrip(',')
#         if where_condition:
#             where_lst = [k + '="' + v + '"' for k, v in where_condition.items()]
#
#             _where = ' and '.join(where_lst) if len(where_lst) > 1 else where_lst[0]
#             where = 'where ' + _where
#         else:
#             where = ''
#         sql = base_sql.format(table=table, updates=updates, where=where)
#         return sql
#
#
#
#
# if __name__ == '__main__':
#     db = BlogDbApi()
#     # sql = 'select * from blog'
#     # datas = db._get_data(sql)
#     # #print(datas)
#     # description = db._get_description(sql)
#     # #如果description 不为空 for循环 遍历 取索引为0的值(也就是字段名) 为空 则调用 _get_fields_meta 方法 取出该表的元数据 字段
#     # ths = [i[0] for i in description ] if description else db._get_fields_meta(schema='blog',table_name='blog')
#     # #print(ths)
#     # #将数据集转换为list
#     # items_list = db._get_list_item(ths=ths,datas=datas)
#     # #print(items_list)
#     sql = db._update(table='x', updates_condition={'title': 'test1', 'db': 'cxy'}, where_condition={'id': '4'})
#     print(sql)







