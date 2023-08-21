import os
import io
from werkzeug.utils import secure_filename
import pymysql
from datetime import datetime
from flask import send_file


def insert(title, user_id, contents, file):
    current_date = datetime.now().date()
    month = current_date.month
    day = current_date.day

    file.save('static/uploads/' + (file.filename))

    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()
    query = "INSERT INTO userTable (title, id, Date, content, file_name, file_data) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query, (title, user_id, f"{month}/{day}", contents, (file.filename), 'static/uploads/'+(file.filename)))
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

def getpost(title, writer):
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT title, id, Date, content, file_name FROM userTable WHERE title = %s AND id = %s"  # 조건이 주어진 경우
    cur.execute(sql, (title, writer))
    data = cur.fetchall()
    conn.close()
    return data


def download_file(file_name):
    conn = pymysql.connect(host='localhost', user='root', password='ckd990518', db='manager', charset='utf8')
    cur = conn.cursor()
    query = "SELECT file_data FROM userTable WHERE file_name = %s"
    cur.execute(query, (file_name,))
    result = cur.fetchone()
    conn.close()
    if result:
        file_data = result[0]
        return send_file(file_data, as_attachment=True)
    else:
        return "File not found"