import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='mydb') # 此处的数据库必须先创建
cursor = conn.cursor()

cursor.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael']) # 注意mysql的占位符是%s
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
print(cursor.fetchall())
