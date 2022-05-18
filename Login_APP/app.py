from sqlite3 import Cursor
from flask import Flask,render_template,request
import mysql.connector
import mysql.connector
from mysql.connector import Error


mydb=mysql.connector.connect(host='s3tomysql.cdn5ytej86t3.us-east-1.rds.amazonaws.com',user='admin',password='admin1234',database='users')
cursor=mydb.cursor()
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/signup',methods=['post','get'])
def signup():
    error=None
    if request.method=="post":
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        dname=request.form.get('dname')
        cname=request.form.get('cname')
        email=request.form.get('email')
        password=request.form.get('pass')
        if len(fname) < 4:
            error="Your firstname should have alteast 6 letters"
        elif len(lname) < 1:
            error="Your lastname should have atleast 1 letter"
        elif len(password) < 6:
            error="Your password should have atleast 6 letters"
        else:
            query=('INSERT INTO userdetails(id,fname,lname,dname,cname,email,password,date) VALUES (NULL,%s,%s,%s,%s,%s,%s,NOW())')
            cursor.execute(query,(fname,lname,dname,cname,email,password))
            mydb.commit()
            #success="Your Account has been created"
    return render_template("signup.html",error=error)


if __name__=='__main__':
    app.run(debug=True)