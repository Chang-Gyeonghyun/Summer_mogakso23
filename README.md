# Summer_mogakso23
## HTML

- 각 페이지 특성에 맞게 html양식을 작성한다.

### home.html

홈페이지를 나타낸다. 

- header에 로고 및 posting, login버튼을 만든다.
- 배경 화면 이미지를 삽입한다.
- Notion과 Github링크를 달아놓는다.
- Search 검색 창으로 게시물의 제목 중 일부를 입력하면  관련 게시물 목록으로 이동한다.
- 참여자의 인물 사진을 걸어두고 해당 버튼을 클릭할 시, 클릭한 대상의 posting 목록으로 이동한다.
- footer 부분에 프로젝트 팀 이름과 기타 사항들을 적어두었다.

### login.html

로그인 페이지를 나타낸다.

- form 양식으로 아이디와 비밀 번호를 입력 받는다.
- 입력 정보가 맞지 않을 경우에는 Password Wrong이라고 알림이 뜬다.
- 입력된 정보는 백엔드 서버로 넘어간다.

### posting.html

게시물 목록을 보여준다.

- header는 홈페이지와 동일하다.
- TOTAL, CHANG, HUN, THING 버튼이 존재하고, 각 버튼을 클릭하였을 때 해당 관리자가 쓴 게시물이 filter 되어 나온다.
- 마찬가지로 title과 writer로 구분하여 검색할 수 있는 창이 존재한다.
- 아무 게시물이 존재하지 않을 경우, There are no registered post.라는 문구가 함께 뜬다.
- 하지만 이전에 게시물을 작성한 적이 있고, DB에 글의 정보가 올라가 있는 상태라면 posting 목록이 생긴다.
- 페이지 수 목록을 나타내는 버튼도 존재했지만, 시간 관계상 만들지 못하였다.

### reading.html

포스팅된 글을 읽는 페이지이다.

- header는 홈페이지와 동일하다.
- 글을 볼 수 있는 제목, 내용 칸이 존재하고, 첨부 파일을 다운할 수 있는 기능이 있다.

### writing.html

글을 작성하는 페이지이다.

- 글을 작성할 수 있는 제목, 내용 칸이 존재하고, 첨부 파일을 함유할 수 있는 기능이 있다.

## Java Script

- 각 특성에 맞게 동적 기능들을 구현한다.

### header.js

html내 header부분의 동적 기능을 담당한다.

- 로고 버튼을 누를 경우, 홈페이지로 이동
- 로그인 버튼을 누를 경우 로그인 페이지로 이동. 로그인 후 버튼은 로그 아웃으로 바뀐다.
- 로그 아웃 버튼을 누를 경우, 웹에서 완전히 로그아웃이 된다.
- posting 버튼을 누를 경우 post 게시물의 목록 창으로 이동한다.
- 검색 창에서 검색 value를 받고, 해당 value에 대해 get메소드로 임의의 url로 이동한다.

### posting.js

posting 부분을 동적 구현한다.

- 각 writer 버튼을 누르면 해당 writer가 쓴 게시물만 보이도록 필터링 한다.
- 게시물을 누르면 해당 정보를 가지고 reading.html로 이동하는 기능을 만든다.

## Python

모든 백엔드, DB 기능을 담당한다.

### main.py

백엔드 서버 기능을 담당한다

- Flask를 통해 파이썬 자체의 백엔드 모듈을 사용한다.
- 관리자 계정의 아이디 비번을 미리 딕셔너리를 통해 만들어준다.
- `@app.route("/", methods=['GET', 'POST'])` 홈페이지로 들어갔을 때, login이 됐는지 아닌지 여부를 판단한다. `render_template("home.html", login=writable)` 으로 home.html을 연다.
- `@app.route("/posting",methods=['GET'])` posting url로 이동하였을 때, posting.html을 연다.
    - posting을 GET 메소드로 받았을 때, sort 목록에 writer인지 title인지 인자를 통해 받고, DB내에 검색하여 해당 리스트를 결과 값으로 받아온다.
- `@app.route("/log-in", methods=['GET', 'POST'])` 로그인 정보를 POST하고  session을 통해 서버 로그인을 진행한다. 이 정보는 서버를 다시 실행시키거나 session에 정보를 임의로 꺼내기 전까지 유지된다. `render_template('login.html', error = error)`
- `@app.route("/writing", methods=['GET', 'POST'])` POST 받으면 해당 name 정보들을 가지고 DB에 넣는 작업을 한다.
    
    ```python
    content = request.form['Content']
                title = request.form['Title']
                file = request.files['File']
                user_id = session['userID']
                insert(title, user_id, content, file)
    ```
    
    `render_template("writing.html", login=writable)`
    
- `@app.route('/logout',methods=['GET'])` 로그아웃 시 session 정보를 꺼내고, 홈페이지로 이동한다.
    
    ```python
    @app.route('/logout',methods=['GET'])
    def logout():
        session.pop('userID',None)
        return redirect('/')
    ```
    
- `@app.route("/reading", methods=['GET'])` 인자로 받은 title과 writer의 정보를 가지고 다시 DB 조회를 시작한다. DB내에서 해당 정보에 맞는 내용 및 첨부 파일을 읽어 오고 html로 정보를 넘겨준다.
- `@app.route("/download",methods=['GET'])` 첨부 파일을 클릭할 시 다운이 되는 기능이다.

### databasePr.py

DB와 관련된 모든 기능을 구현현다.

- `def insert(title, user_id, contents, file)` 인자로 받은 값들을 바탕으로 DB에 넣는 역할을 한다.
    
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
    
    Date를 통해서 현재 날짜 정보를 받아온다.
    
    pymysql모듈을 사용하여 파이썬을 통해 mysql 데이터베이스를 접근할 수 있다.
    
    파일 접근은 파일 명을 받아오고 해당 파일을 서버 자체 임의의 경로에 저장한다. 그리고 파일 경로를 DB값으로 저장한다.
    
- `def getdata(title=False, id=False, value=None):` DB값을 조회하고 가져오는 함수이다.
    - `"SELECT title, id, Date FROM userTable”` 코드를 활용하여 원하는 데이터만 추출할 수 있다
- `def getpost(title, writer):` 이는 게시물을 클릭했을 때 내용 및 상세 정보를 보기 위해 DB에서 더욱 상세한 값들을 추출하는 단계이다.
- `def download_file(file_name):`  먼저 파일 경로를 통해 해당 파일에 접근하고, `send_file(file_data, as_attachment=True)`을 이용하여 파일을 다운받는다.