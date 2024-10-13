from templates.config import conn

cur = conn.cursor()


def add_user(name, username, password):
    # sql commands
    sql = "INSERT INTO user(name, username, password) VALUES ('%s','%s','%s')" % (name, username, password)
    # execute(sql)
    cur.execute(sql)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()







