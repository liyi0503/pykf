import pymysql
import pymysql
import os

from common.myConf import MyConf
from common.my_path import conf_dir


class MysqlUtil:
    # 初始化函数
    def __init__(self):
        # 连接mysql数据库
        conf = MyConf(os.path.join(conf_dir, "mysql.ini"))
        # 连接数据库/生成游标
        self.coon = pymysql.connect(
            host=conf.get("mysql", "host"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "passwd"),
            port=conf.getint("mysql", "port"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,

        )
        # 设置自动提交
        self.coon.autocommit(True)
        # 获取游标对象
        self.cursor = self.coon.cursor()

    # 查询 select * from user
    def query(self, sql, params=None):
        # 执行sql
        self.cursor.execute(sql, params)
        # 获取查询的所有数据
        return self.cursor.fetchall()

    # 增删改---update更新数据库函数
    def update(self, sql, params=None):

        try:
            # 执行sql语句
            self.cursor.execute(sql, params)
            # 提交
            self.conn.commit()
        except Exception as result:
            print(result)
            # 回滚
            self.conn.rollback()

    # 关闭函数
    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()


if __name__ == '__main__':
    ms = MysqlUtil()
    s = ms.query("select * from student where name='叮当'")
    print(s)
