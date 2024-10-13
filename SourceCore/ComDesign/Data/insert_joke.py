import pymysql.cursors
import pandas as pd
#连接数据库
connect = pymysql.Connect(
    host='localhost',  # 主机名
    port= 3306,  # 端口号
    user='root',  # 数据库用户名
    passwd='123456',  # 密码
    db='recommand',  # 数据库名称
    charset='utf8'  # 编码格式
)
# 获取游标
print("连接成功")
cursor = connect.cursor()
#如果表已存在，则先删除此表
cursor.execute("drop table if exists joke")
print("delete successfully")

#设定sql语句
#创建表 采用自增id号AUTO_INCREMENT
sql = """
create table joke(
    id  INT AUTO_INCREMENT primary key,
    text varchar(1000));
"""

#执行sql语句
cursor.execute(sql)
print("表创建成功")


# print(cursor.execute("describe jokedata;"))

#关闭数据库连接
connect.close()

# 读取csv文件
df = pd.read_csv('joke.csv')

# 定义需要去除的字符
chars_to_remove = ['<', '>', '/', 'p']

# 遍历每一列，使用replace函数去除特定字符
for col in df.columns:
    for char in chars_to_remove:
        df[col] = df[col].astype(str).str.replace(char, '')

# 保存处理后的csv文件
df.to_csv('./joke_cleaned.csv', index=False)

# 读取csv文件
data = pd.read_csv('./joke_cleaned.csv',encoding='utf8')

# 连接到MySQL数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', database='recommand', charset='utf8')
cursor = conn.cursor()

# 将数据插入到jokedata表中
#id = 0
for index, row in data.iterrows():
 #   id = id+1
    sql = f"INSERT INTO joke (text) VALUES ('{row['text']}')"
    cursor.execute(sql)

# 提交事务
conn.commit()
# 关闭连接
cursor.close()
conn.close()



