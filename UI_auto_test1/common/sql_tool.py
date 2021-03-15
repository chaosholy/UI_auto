# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/2   15:50
============================
"""
import pymysql
from common.conf import conf


class SqlTool:
    def sqlRead(self, sql):
        conn = pymysql.connect(host=conf("sql", "host"),
                               port=int(conf("sql", "port")),
                               user=conf("sql", "username"),
                               password=conf("sql", "psw"),
                               charset='utf8'
                               )
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        value = cur.fetchall()
        return value
