"""
1.SQLite数据库
Python内置了SQLite3，所以直接导入即可使用。

优点：简单轻便 
确定：不适合高并发访问

代码:(先创建数据库并插入一些数据)
"""


import sqlite3

# 建表语句
create_table = """create table if not exists user(
    id varchar(200) primary key,
    name varchar(20)
);
"""

# 插入语句
insert_sql = 'insert into user (id,name) values (?,?)'

conn = sqlite3.connect('mytest.db')  # 如果数据库不存在，则再当前文件夹下创建
cursor = conn.cursor()  # 获取游标
cursor.execute(create_table)  # 执行sql语句，同其他大多数
cursor.execute(insert_sql, ('1', 'jack'))
cursor.execute(insert_sql, ('2', 'tom'))
cursor.execute(insert_sql, ('3', 'lili'))
cursor.close()  # 关闭cursor
conn.commit()  # 修改数据库之后要commit，否则关闭数据库后无法查询到更改的数据
conn.close()  # 关闭数据库连接


# 查询语句
# 插入语句
insert_sql = 'insert into user (id,name) values (?,?)'

conn = sqlite3.connect('mytest.db')  # 如果数据库不存在，则再当前文件夹下创建
cursor = conn.cursor()  # 获取游标
cursor.execute(create_table)  # 执行sql语句，同其他大多数
cursor.execute(insert_sql, ('1', 'jack'))
cursor.execute(insert_sql, ('2', 'tom'))
cursor.execute(insert_sql, ('3', 'lili'))
cursor.close()  # 关闭cursor
conn.commit()  # 修改数据库之后要commit，否则关闭数据库后无法查询到更改的数据
conn.close()  # 关闭数据库连接
