from templates.config import conn

cur = conn.cursor()


def is_null(username, password):
    if username == '' or password == '':
        return True
    else:
        return False


def is_existed(username, password):
    sql = "SELECT * FROM user WHERE username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        print('false')
        return False
    else:
        print('true')
        return True


def exist_user(username):
    sql = "SELECT * FROM user WHERE username ='%s'" % (username)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True

