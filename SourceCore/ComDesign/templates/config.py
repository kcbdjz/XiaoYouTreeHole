# 数据库连接配置
import pymysql
import pymongo
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('D:\学习\pycharm_workspase\ComDesign\config.ini')
mysql = cfg.items('mysql')
conn = pymysql.connect(
    host=mysql[0][1],  # 主机名
    port=eval(mysql[1][1]),  # 端口号
    user=mysql[2][1],  # 数据库用户名
    password=mysql[3][1],  # 密码
    database=mysql[4][1],  # 数据库名称
    charset=mysql[5][1]  # 编码格式
)
mongodb = cfg.items('mongodb')
client = pymongo.MongoClient(host=mongodb[0][1], port=eval(mongodb[1][1]))
db = client[mongodb[2][1]]
