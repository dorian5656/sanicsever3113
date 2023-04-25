#! /usr/bin/env python
# -*-coding:utf-8-*-
import pandas as pd
import psycopg2

# Pg数据库工具
class Postgre_Curd(object):
    """
    pg数据库增删改查
    """
    def __init__(self, host="", port="", user="", password="", database=""):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def get_pg_version(self):
        """
        查询pg版本号
        :return:
        """
        # 连接到Postgre数据库
        conn = psycopg2.connect(
            host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

        # 打开游标
        cur = conn.cursor()

        # 查询PostgreSQL版本
        cur.execute(F"SELECT version();")
        version = cur.fetchone()

        print(version)

        # 关闭游标和连接
        cur.close()
        conn.close()
        return version

    def select_data_sql(self, sql_query):
        """
        sql语句查询
        :param sql_query:  请求的sql
        :return: 查询的数据
        """

        # 创建连接
        conn = psycopg2.connect(
            host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

        # 游标
        cur = conn.cursor()
        cur.execute(sql_query)

        # 获取全部值
        data = cur.fetchall()
        cur.close()
        conn.close()
        print(data)
        return data

    def select_data_pd(self, sql_query):
        """
        sql语句查询
        :param sql_query:  请求的sql
        :return: 查询的数据
        """

        # 创建连接
        conn = psycopg2.connect(
            host=self.host, port=self.port, database=self.database, user=self.user, password=self.password)

        df = pd.read_sql(sql_query, conn)
        # 关闭连接
        conn.close()
        # 打印数据框架的前几行
        print(df.head())
        return df


# if __name__ == '__main__':
#     from FileTools.YmlTools import YmlCurd
#     pg_serve_info = "../ConfigTools/DatabaseConfig/PgServe.yml"
#     FC = YmlCurd(pg_serve_info)
#     res_yml = FC.read_yaml()
#     pg = res_yml['pg']
#     PC = Postgre_Curd(pg.get("host"), pg.get("port"), pg.get("username"), pg.get("password"), pg.get("database"))
#     PC.get_pg_version()  # 测试链接Pg库
#     sql_query = F"SELECT version();"
#     pg_data = PC.select_data_sql(sql_query)
    # df = PC.select_data_pd(sql_query)
