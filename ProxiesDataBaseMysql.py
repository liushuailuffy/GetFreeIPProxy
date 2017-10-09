# coding = utf-8
import pymysql
import traceback

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'proxies',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

#初始化建表
def InitDB():
    #connect to the datebase
    db = pymysql.connect(**config)
    #使用cursor()方法获取操作游标
    cursor = db.cursor()
    #sql语句
    sql = "CREATE TABLE IF NOT EXISTS IPPORT (IP_PORT TEXT NOT NULL)"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        print("出现错误啦~错误是：",e)
        #发生错误则回滚
        db.rollback()
        return False
    #关闭数据库
    db.close()

def AddItem(ip_port):
    print("进入AddItem()")
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO IPPORT VALUES(%s)"
    try:
        cursor.execute(sql,(ip_port))
        db.commit()
    except Exception as e:
        print("出现错误啦~错误是：",e)
        db.rollback()
        traceback.print_exc()
    db.close()

def AddItems(ip_list):
    if len(ip_list) < 1:
        return

    sql_str = """INSERT INTO IPPORT VALUES """
    for item in ip_list:
        sql_str += ("('{}'),".format(item))
    index = len(sql_str)
    sql_str = sql_str[0:index - 1]
    sql_str += ";"
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        cursor.execute(sql_str)
        db.commit()
    except Exception as e:
        print("出现错误啦~错误是：",e)
        db.rollback()
        traceback.print_exc()
    db.close()

def DelItem(item):
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "DELETE FROM IPPORT WHERE IP_PORT=%s"
    try:
        cursor.execute(sql,(item))
        db.commit()
    except Exception as e:
        print("出现错误啦~错误是：",e)
        db.rollback()
        traceback.print_exc()
    db.close()

def ClearItems():
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "DELETE FROM IPPORT"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("出现错误啦~错误是：",e)
        db.rollback()
        traceback.print_exc()
    db.close()

def GetItems():
    ip_list = []
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM IPPORT"
    try:
        cursor.execute(sql)
        for item in cursor.fetchall():
            print(item['IP_PORT'])
            ip_list.append(item['IP_PORT'])
    except Exception as e:
        print("出现错误啦~错误是：",e)
        traceback.print_exc()
    db.close()
    return ip_list
