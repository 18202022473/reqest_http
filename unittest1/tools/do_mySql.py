import mysql.connector  # pip install mysql-connector
from lemon.unittest1.tools.config import Config
from lemon.unittest1.tools.project_path import config_path


class DoMysql:
    def do_mysql(self, query_sql, state='all'):
        # 创建一个数据库连接
        cnn = mysql.connector.connect(**eval(Config().config(config_path, 'DB', 'db_config')))

        # 游标cursor
        cursor = cnn.cursor()
        # 写sql语句--字符串
        # query_sql = 'select * from member where MobilePhone = 13755127762'
        # 执行语句
        cursor.execute(query_sql)
        # 获取打印结果
        if state == 1:
            res = cursor.fetchone()  # 元组 针对一条数据
        else:
            res = cursor.fetchall()  # 列表 针对多行数据 列表嵌套元组
        # print(res)
        # 关闭游标
        cursor.close()
        # 关闭连接
        cnn.close()
        return res


if __name__ == '__main__':
    print(DoMysql().do_mysql('select * from member where MobilePhone = 13755127762'))
