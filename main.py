from flask import Flask, render_template, request, redirect, send_file, session, url_for
from extractor.databasePr import insert, getdata


app = Flask(__name__) #플라스크 애플리케이션을 생성
app.secret_key = "adfafsafsafsa1"

manager= {
    "Chang":"0416",
    "Hun": "1234",
    "Thing": "0128"
}

@app.route("/", methods=['GET', 'POST'])
def home(): 
    writable = False
    if 'userID' in session:
        writable = True
    return render_template("home.html", login=writable)



@app.route("/posting",methods=['GET'])
def search():
    writable = False
    Isdata = False
    if request.method == 'GET':
        sort = request.args.get("sort")      # sort 변수에 "writer"가 저장될 것
        subject = request.args.get("subject")
        if sort and sort == "title":
            result = getdata(True, False, subject)
        elif sort and sort == "writer":
            result = getdata(False, True, subject)
        else:
            result = getdata()
            
        if result:
            Isdata = True
            return render_template("posting.html", writable=writable, Isdata=Isdata, items=reversed(result))
    if session['userID']:
        writable = True
    return render_template("posting.html", writable=writable, Isdata=Isdata) #{%%}는 html내에 python코드를 넣게 해준다.


@app.route("/log-in", methods=['GET', 'POST'])
def login():
    error = None
    global manager
    if request.method == 'POST':
        username = request.form.get("userName")
        userpassword = request.form.get("userPassword")
        
        if manager[username] == userpassword:
            session["userID"] = username
            return redirect(url_for("home"))
        else:
            error = 'invalid input data detected !'
            
    return render_template('login.html', error = error)


@app.route("/writing", methods=['GET', 'POST'])
def writing():
    if request.method == 'POST': # 게시판에 글 등록하기
        content = request.form['content']
        id = session['userID']
        insert(content,id)
        return redirect(url_for("search"))
    return render_template("writing.html")

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userID',None)
    return redirect('/')


app.run("127.0.0.1")