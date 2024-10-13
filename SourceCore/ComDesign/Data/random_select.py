import pymysql


def random_select(table_name):
    result = None

    connection = pymysql.connect(host='localhost',  # 主机名
                                 port=3306,  # 端口号
                                 user='root',  # 数据库用户名
                                 passwd='123456',  # 密码
                                 db='recommand',  # 数据库名称
                                 charset='utf8'  # 编码格式
                                 )

    # 获取游标
    cursor = connection.cursor()

    # 设置随机数范围
    min_value = 1
    max_value = 16

    # 随机查看一条记录的 SQL 语句
    sql = "SELECT * FROM {} WHERE id >= %s AND id <= %s ORDER BY RAND() LIMIT 1".format(table_name)

    try:
        # 执行查询
        cursor.execute(sql, (min_value, max_value))

        # 获取结果
        result = cursor.fetchone()

        if result:
            print("随机查看的记录：", result)
        else:
            print("数据库中没有符合条件的记录！")

    except Exception as e:
        print("查询失败:", e)

    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()
    return result