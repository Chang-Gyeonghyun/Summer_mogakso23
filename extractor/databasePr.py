import pymysql
from datetime import datetime

def insert(title, user_id, contents):
    current_date = datetime.now().date()
    month = current_date.month
    day = current_date.day
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()
    query = "INSERT INTO userTable (title, id, Date, content) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (title, user_id, month + "/" + day, contents))
    conn.commit()
    conn.close()

    
def getdata(title=False, id=False, value=None):
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()

    if title:
        sql = "SELECT title, id FROM userTable WHERE title LIKE %s"  # 조건이 주어진 경우
        cur.execute(sql, ('%' + value + '%',))
        
    elif id:
        if value == "TOTAL":
            sql = "SELECT title, id, Date FROM userTable"  # 조건이 주어지지 않은 경우
            cur.execute(sql)
        else:
            sql = "SELECT title, id, Date FROM userTable WHERE id = %s"  # 조건이 주어진 경우
            cur.execute(sql, (value))
    else:
        sql = "SELECT title, id, Date FROM userTable"  # 조건이 주어지지 않은 경우
        cur.execute(sql)
        
    data = cur.fetchall()
    conn.close()
    return data