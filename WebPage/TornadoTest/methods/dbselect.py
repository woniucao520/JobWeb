# coding:utf-8

def _select(columns, db_name, table_name, where=None):
    base_sql = r"select {select_str} from {db_name}.{table_name} {where_str}"

    _columns = ','.join(columns).rstrip(',')
    if where:
        _where = [k + '=' + v for k, v in where.items()]
        if len(_where) > 1:
            _where_str = 'where ' + ' and '.join(_where)
        else:
            _where_str = 'where ' + _where[0]
    else:
        _where_str = ''
    sql = base_sql.format(select_str=_columns, db_name=db_name, table_name=table_name, where_str=_where_str)
    print("拼接的sql", sql)
    return sql


if __name__ == '__main__':
    _select()