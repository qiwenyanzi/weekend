# 1.导入pymysql代码库
import pymysql


def connect_db():
    # 要想连接数据库，需要知道数据库的：ip地址，端口号，用户名和密码，数据库名称
    conn = pymysql.Connect(host='localhost', user='root', password="root", database='pirate', port=3306, charset='utf8')
    # 查询hd_user表中所有的数据，并按id倒叙
    sql = 'select * from hd_user order by id desc'
    # 要想在代码中执行这条sql语句，首先要获取数据库的游标cursor
    curs = conn.cursor()
    # 通过游标执行sql语句
    curs.execute(sql)
    # 得到结果，获取最新一条数据,用fetchone()获取第一条记录
    result = curs.fetchone()
    #fetchall()获取所以的查询结果
    return result
if __name__ == '__main__':
    print(connect_db())