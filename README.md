# Summer_mogakso23
## HTML

- �� ������ Ư���� �°� html����� �ۼ��Ѵ�.

### home.html

Ȩ�������� ��Ÿ����. 

- header�� �ΰ� �� posting, login��ư�� �����.
- ��� ȭ�� �̹����� �����Ѵ�.
- Notion�� Github��ũ�� �޾Ƴ��´�.
- Search �˻� â���� �Խù��� ���� �� �Ϻθ� �Է��ϸ�  ���� �Խù� ������� �̵��Ѵ�.
- �������� �ι� ������ �ɾ�ΰ� �ش� ��ư�� Ŭ���� ��, Ŭ���� ����� posting ������� �̵��Ѵ�.
- footer �κп� ������Ʈ �� �̸��� ��Ÿ ���׵��� ����ξ���.

### login.html

�α��� �������� ��Ÿ����.

- form ������� ���̵�� ��� ��ȣ�� �Է� �޴´�.
- �Է� ������ ���� ���� ��쿡�� Password Wrong�̶�� �˸��� ���.
- �Էµ� ������ �鿣�� ������ �Ѿ��.

### posting.html

�Խù� ����� �����ش�.

- header�� Ȩ�������� �����ϴ�.
- TOTAL, CHANG, HUN, THING ��ư�� �����ϰ�, �� ��ư�� Ŭ���Ͽ��� �� �ش� �����ڰ� �� �Խù��� filter �Ǿ� ���´�.
- ���������� title�� writer�� �����Ͽ� �˻��� �� �ִ� â�� �����Ѵ�.
- �ƹ� �Խù��� �������� ���� ���, There are no registered post.��� ������ �Բ� ���.
- ������ ������ �Խù��� �ۼ��� ���� �ְ�, DB�� ���� ������ �ö� �ִ� ���¶�� posting ����� �����.
- ������ �� ����� ��Ÿ���� ��ư�� ����������, �ð� ����� ������ ���Ͽ���.

### reading.html

�����õ� ���� �д� �������̴�.

- header�� Ȩ�������� �����ϴ�.
- ���� �� �� �ִ� ����, ���� ĭ�� �����ϰ�, ÷�� ������ �ٿ��� �� �ִ� ����� �ִ�.

### writing.html

���� �ۼ��ϴ� �������̴�.

- ���� �ۼ��� �� �ִ� ����, ���� ĭ�� �����ϰ�, ÷�� ������ ������ �� �ִ� ����� �ִ�.

## Java Script

- �� Ư���� �°� ���� ��ɵ��� �����Ѵ�.

### header.js

html�� header�κ��� ���� ����� ����Ѵ�.

- �ΰ� ��ư�� ���� ���, Ȩ�������� �̵�
- �α��� ��ư�� ���� ��� �α��� �������� �̵�. �α��� �� ��ư�� �α� �ƿ����� �ٲ��.
- �α� �ƿ� ��ư�� ���� ���, ������ ������ �α׾ƿ��� �ȴ�.
- posting ��ư�� ���� ��� post �Խù��� ��� â���� �̵��Ѵ�.
- �˻� â���� �˻� value�� �ް�, �ش� value�� ���� get�޼ҵ�� ������ url�� �̵��Ѵ�.

### posting.js

posting �κ��� ���� �����Ѵ�.

- �� writer ��ư�� ������ �ش� writer�� �� �Խù��� ���̵��� ���͸� �Ѵ�.
- �Խù��� ������ �ش� ������ ������ reading.html�� �̵��ϴ� ����� �����.

## Python

��� �鿣��, DB ����� ����Ѵ�.

### main.py

�鿣�� ���� ����� ����Ѵ�

- Flask�� ���� ���̽� ��ü�� �鿣�� ����� ����Ѵ�.
- ������ ������ ���̵� ����� �̸� ��ųʸ��� ���� ������ش�.
- `@app.route("/", methods=['GET', 'POST'])` Ȩ�������� ���� ��, login�� �ƴ��� �ƴ��� ���θ� �Ǵ��Ѵ�. `render_template("home.html", login=writable)` ���� home.html�� ����.
- `@app.route("/posting",methods=['GET'])` posting url�� �̵��Ͽ��� ��, posting.html�� ����.
    - posting�� GET �޼ҵ�� �޾��� ��, sort ��Ͽ� writer���� title���� ���ڸ� ���� �ް�, DB���� �˻��Ͽ� �ش� ����Ʈ�� ��� ������ �޾ƿ´�.
- `@app.route("/log-in", methods=['GET', 'POST'])` �α��� ������ POST�ϰ�  session�� ���� ���� �α����� �����Ѵ�. �� ������ ������ �ٽ� �����Ű�ų� session�� ������ ���Ƿ� ������ ������ �����ȴ�. `render_template('login.html', error = error)`
- `@app.route("/writing", methods=['GET', 'POST'])` POST ������ �ش� name �������� ������ DB�� �ִ� �۾��� �Ѵ�.
    
    ```python
    content = request.form['Content']
                title = request.form['Title']
                file = request.files['File']
                user_id = session['userID']
                insert(title, user_id, content, file)
    ```
    
    `render_template("writing.html", login=writable)`
    
- `@app.route('/logout',methods=['GET'])` �α׾ƿ� �� session ������ ������, Ȩ�������� �̵��Ѵ�.
    
    ```python
    @app.route('/logout',methods=['GET'])
    def logout():
        session.pop('userID',None)
        return redirect('/')
    ```
    
- `@app.route("/reading", methods=['GET'])` ���ڷ� ���� title�� writer�� ������ ������ �ٽ� DB ��ȸ�� �����Ѵ�. DB������ �ش� ������ �´� ���� �� ÷�� ������ �о� ���� html�� ������ �Ѱ��ش�.
- `@app.route("/download",methods=['GET'])` ÷�� ������ Ŭ���� �� �ٿ��� �Ǵ� ����̴�.

### databasePr.py

DB�� ���õ� ��� ����� ��������.

- `def insert(title, user_id, contents, file)` ���ڷ� ���� ������ �������� DB�� �ִ� ������ �Ѵ�.
    
    ```python
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
    ```
    
    Date�� ���ؼ� ���� ��¥ ������ �޾ƿ´�.
    
    pymysql����� ����Ͽ� ���̽��� ���� mysql �����ͺ��̽��� ������ �� �ִ�.
    
    ���� ������ ���� ���� �޾ƿ��� �ش� ������ ���� ��ü ������ ��ο� �����Ѵ�. �׸��� ���� ��θ� DB������ �����Ѵ�.
    
- `def getdata(title=False, id=False, value=None):` DB���� ��ȸ�ϰ� �������� �Լ��̴�.
    - `"SELECT title, id, Date FROM userTable��` �ڵ带 Ȱ���Ͽ� ���ϴ� �����͸� ������ �� �ִ�
- `def getpost(title, writer):` �̴� �Խù��� Ŭ������ �� ���� �� �� ������ ���� ���� DB���� ���� ���� ������ �����ϴ� �ܰ��̴�.
- `def download_file(file_name):`  ���� ���� ��θ� ���� �ش� ���Ͽ� �����ϰ�, `send_file(file_data, as_attachment=True)`�� �̿��Ͽ� ������ �ٿ�޴´�.