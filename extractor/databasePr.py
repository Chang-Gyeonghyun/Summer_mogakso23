import pymysql

def insert(content, user_id):
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()
    query = "INSERT INTO userTable (content, id) VALUES (%s, %s)"
    cur.execute(query, (content, user_id))
    conn.commit()
    conn.close()

    
def getdata(title=False, id=False, value=None):
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()

    if title:
        sql = "SELECT content, id FROM userTable WHERE content LIKE %s"  # 조건이 주어진 경우
        cur.execute(sql, ('%' + value + '%',))
        
    elif id:
        if value == "TOTAL":
            sql = "SELECT content, id FROM userTable"  # 조건이 주어지지 않은 경우
            cur.execute(sql)
        else:
            sql = "SELECT content, id FROM userTable WHERE id = %s"  # 조건이 주어진 경우
            cur.execute(sql, (value))
    else:
        sql = "SELECT content, id FROM userTable"  # 조건이 주어지지 않은 경우
        cur.execute(sql)
        
    data = cur.fetchall()
    conn.close()
    return data