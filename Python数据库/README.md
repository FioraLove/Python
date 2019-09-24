## 一、Python与MySQL数据库连接

    # -*- coding:utf-8 -*-
    import pymysql
    
#### 法一：普通脚本编写

    # 1.创建与数据库连接对象
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           database="db4",
                           charset="utf8")

    # 2.利用db方法创建游标对象
    cursor = conn.cursor()

    # 3.利用游标对象execute()方法执行SQL命令
    # cur.execute("sql语句") #这里填写正确的SQL语句  例如:
    cursor.execute("insert into sheng values(16,300000,'台湾省');")
    # 4.除select查找操作以外的操作都需要提交到数据库执行
    conn.commit()
    print("OK")
    # 5.关闭游标对象
    cursor.close()

    # 6.断开数据库连接
    conn.close()


#### 法二:封装成一个类，使用更加方便，就可以在别的地方直接导入就可以使用了(from … import…)
    class MysqlPython(object):
        def __init__(self, database, host="localhost", user="root",
                     password="123456", port=3306, charset="utf8"):
            self.host = host
            self.user = user
            self.password = password
            self.port = port
            self.database = database
            self.charset = charset

        # 数据库连接方法:
        def open(self):

            self.conn = pymysql.connect(host=self.host, user=self.user,
                                        password=self.password, port=self.port,
                                        database=self.database, charset=self.charset)
            # 游标对象
            cursor = self.conn.cursor()
            if not cursor:
                return (NameError, "连接数据库失败")
            else:
                return cursor

        # 数据库执行操作方法:
        def ExecQuery(self, sql):  # 获取数据库连接信息
            try:
                cur = self.open()
                # 执行SQL语句操作
                cur.execute(sql)
                # 获取所有的查询结果
                response = cur.fetchall()
                self.conn.commit()
                print("ok")
                return response
            except Exception as e:
                self.conn.rollback()
                print("Failed:", e)

            # 数据库关闭方法:
            cursor.close()
            self.conn.close()
