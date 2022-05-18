
from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
import pymysql
import re
#from flask_mysqldb import MySQL
#import MySQLdb.cursors

#from flaskext.mysql import MySQL
'''mysql = MySQL()
app=Flask(__name__)
app.config['MYSQL_HOST']='se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='suma1234'
app.config['MYSQL_DB']='SIGNUP'
app.config['MYSQL_PORT']=3306
#app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)'''
HOST='se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com'
USERNAME='admin'
PASSWORD='suma1234'
DB='SIGNUP'

#mysql.init_app(app)
#Login
app=Flask(__name__)

'''@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        #cur=pymysql.connection.cursor()
        #cur = mysql.get_db().cursor()
        conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
        cur=conn.cursor() 
        cur.execute("select * from userdetails where email=%s and password=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["UNAME"]
            flash('Login Successfully','success')
            return redirect('home')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")
  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap'''
 
#Registration  
@app.route('/') 
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    msg=''
    #if request.method=='POST':
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'dname' in request.form and 'cname' in request.form and 'email' in request.form and 'upass' in request.form:

        First_Name=request.form["fname"]
        Last_Name=request.form["lname"]
        Department_Name=request.form["dname"]
        Client_Name=request.form["cname"]
        Email=request.form["email"]
        Password=request.form["upass"]
        conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
        cur=conn.cursor() 
        cur.execute('SELECT * FROM userdetails WHERE email = % s', (Email, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
            msg = 'Invalid email address !'
        elif not Password or not Email:
            msg = 'Please fill out the form !'
        else:
            cur.execute('INSERT INTO userdetails VALUES (NULL, % s, % s, % s,% s, % s, % s)', (First_Name,Last_Name,Department_Name,Client_Name,Email,Password, ))
            conn.commit()
            conn.close()
            msg='Registration Successfully'
        return redirect('login')
            
    return render_template('reg.html', msg=msg)
'''cur.execute("insert into userdetails(First_Name,Last_Name,Department_Name,Client_Name,Email,Password) values(%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Department_Name,Client_Name,Email,Password))
conn.commit()
conn.close()
flash('Registration Successfully. Login Here...','success')
return redirect('login')
return render_template("reg.html",status=status)'''


@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        #cur=pymysql.connection.cursor()
        #cur = mysql.get_db().cursor()
        conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
        cur=conn.cursor() 
        cur.execute("select * from userdetails where Email=%s and Password=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['id'] = data[0]
            session['username']= data[1]
            flash('Login Successfully','success')
            return redirect('home')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")
  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap

#Home page
@app.route("/home")
@is_logged_in
def home():
	return render_template('home.html')
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))
    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)