import pymysql

def delete_record_from_table(table_name, record_id):
    # 连接到MySQL数据库
    db = pymysql.connect(
        host='localhost',  # 主机名
        port=3306,  # 端口号
        user='root',  # 数据库用户名
        passwd='123456',  # 密码
        db='recommand',  # 数据库名称
        charset='utf8'  # 编码格式
    )

    # 创建游标对象
    cursor = db.cursor()

    # 删除数据
    delete_query = f"DELETE FROM {table_name} WHERE id = %s"
    cursor.execute(delete_query, (record_id,))

    # 提交更改并关闭连接
    db.commit()
    print("删除成功")
    db.close()

# 假设你要删除表中id为2的记录
table_name = input("请输入表名：")
record_id_to_delete = input("请输入id:")

# 调用函数删除指定数据
delete_record_from_table(table_name, record_id_to_delete)