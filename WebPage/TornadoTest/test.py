# coding:utf-8

# columns = ['id']
# _columns1 = ','.join(columns)
# print('_columns1::::',_columns1)
# _columns2 = ','.join(columns).rstrip(',')
# print(_columns2)
# columns = ['id','id3']
# _columns3 = ','.join(columns)
# print(_columns3)
# _columns4 = ','.join(columns).rstrip(',')
# print(_columns4)

# _where= ['id="4"','id3="5"']
# result = 'where ' + ' and '.join(_where)
# print (result)

# coding:utf-8

# def _select(columns, db_name, table_name, where=None):
#     base_sql = r"select {select_str} from {db_name}.{table_name} {where_str}"
#
#     _columns = ','.join(columns).rstrip(',')
#     if where:
#         _where = [k + '=' + v for k, v in where.items()]
#         if len(_where) > 1:
#             _where_str = 'where ' + ' and '.join(_where)
#         else:
#             _where_str = 'where ' + _where[0]
#     else:
#         _where_str = ''
#     sql = base_sql.format(select_str=_columns, db_name=db_name, table_name=table_name, where_str=_where_str)
#     print("拼接的sql", sql)
#     return sql
#
#
# if __name__ == '__main__':
#     _select()
    # columns = ['id', 'id3']
    # sql1 = _select(columns=columns, db_name='x', table_name='y', where=None)
    # print(sql1)
    # sql2 = _select(columns=columns, db_name='x', table_name='y', where={'id': '4'})
    # print(sql2)
    # sql3 = _select(columns=columns, db_name='x', table_name='y', where={'id': '4', 'id3': '5'})
    # print(sql3)

# a = ["id","name","age"]
# b = ("1","cxue","25")
# result = dict(zip(a,b))
# print (result)

result = [{'id': 26, 'title': 'Python数据处理-巧用Excel-Python生成SQL脚本'}, {'id': 27, 'title': 'Python数据处理-清洗处理txt文件存储的不规范json数据'}]

for i in result:
    print(i['id'])