

import pymysql


def get_users():
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='12345678', database='mydb_test')
    # 创建游标
    cursor = conn.cursor()
    # 执行SQL语句
    cursor.execute("SELECT * FROM my_users ")
    # 获取查询结果
    rows = cursor.fetchall()
    # 关闭游标和连接
    cursor.close()
    conn.close()
    print(f'users: {rows}')
    return  rows

def add_user():
    coon = pymysql.connect(host='localhost', user='root', password='12345678', database='mydb_test', autocommit=True)

    # 创建游标
    cursor = coon.cursor()

    # 执行SQL语句 新增数据 并返回影响行数
    rows = cursor.execute('INSERT INTO my_users(username, password,status) VALUES ("wulala", "654321",true)')

    # 手动提交
    # coon.commit()

    # 打印结果
    print(rows)

    # 关闭游标和连接
    cursor.close()
    coon.close()

def modify_user():
    coon = pymysql.connect(host='localhost', user='root', password='12345678', database='mydb_test', autocommit=True)

    # 创建游标
    cursor = coon.cursor()

    # 执行SQL语句 新增数据 并返回影响行数
    rows = cursor.execute('UPDATE my_users SET password="7758258" WHERE username="jaye3"')

    # 手动提交
    # coon.commit()

    # 打印结果
    print(rows)

    # 关闭游标和连接
    cursor.close()
    coon.close()

def delete_user():
    coon = pymysql.connect(host='localhost', user='root', password='12345678', database='mydb_test', autocommit=True)

    # 创建游标
    cursor = coon.cursor()

    # 执行SQL语句 新增数据 并返回影响行数
    rows = cursor.execute('DELETE FROM my_users WHERE username="wulala"')

    # 手动提交
    # coon.commit()

    # 打印结果
    print(rows)

    # 关闭游标和连接
    cursor.close()
    coon.close()

# add_user()
# modify_user()
# delete_user()

users = get_users()
for user in users:
    print(f'user: {user}')