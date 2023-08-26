from flask import Flask, render_template, request, redirect, session, url_for
from extractor.databasePr import insert, getdata, getpost, download_file



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
    subject = ""
    writable = False
    Isdata = False
    if 'userID' in session:
        writable = True
    if request.method == 'GET':
        sort = request.args.get("sort")      # sort 변수에 "writer"가 저장될 것
        subject = request.args.get("subject")
        if sort and sort == "title":
            result = getdata(True, False, subject)
        elif sort and sort == "writer":
            result = getdata(False, True, subject)
        else:
            result = getdata()
        if not subject:
            subject = "TOTAL"
        if result:
            Isdata = True
            if subject == "TOTAL":
                arg = "TOTAL"
            else:
                arg = result[0][1]
            return render_template("posting.html", login=writable, Isdata=Isdata, items=reversed(result), subject = arg)
    return render_template("posting.html", login=writable, Isdata=Isdata,subject=subject) #{%%}는 html내에 python코드를 넣게 해준다.


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
    writable = False
    if 'userID' in session:
        writable = True
    if request.method == 'POST':
        if request.form.get("Back"):
            return redirect(url_for("search"))
        else:
            content = request.form['Content']
            title = request.form['Title']
            file = request.files['File']
            user_id = session['userID']
            insert(title, user_id, content, file)

        return redirect(url_for("search"))

    return render_template("writing.html", login=writable)

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userID',None)
    return redirect('/')

@app.route("/reading", methods=['GET'])
def reading():
    writable = False
    if 'userID' in session:
        writable = True
    title = request.args.get("title")
    writer = request.args.get("writer")
    data = getpost(title,writer)
    return render_template("reading.html",login=writable, data=data[0])

@app.route("/download",methods=['GET'])
def downloading():
    file_name = request.args.get("file_name")
    return download_file(file_name)


app.run("127.0.0.1")