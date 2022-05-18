# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import pymysql
import re
import boto3
from werkzeug.utils import secure_filename
import mysql.connector

ACCESS_KEY = 'AKIAYOTRUKBAV6ESOUUN'
SECRET_KEY = 'RI9jbsopUiEPI0A10BH5bIgsUDaq2qxyYe42OD9C'


app = Flask(__name__)


#app.secret_key = 'your secret key'

'''app.config['MYSQL_HOST'] = 'se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin1234'
app.config['MYSQL_DB'] = 'SIGNUP'
app.config['MYSQL_PORT']=3306
#app.config['OPTIONS']: {'ssl', False}'''

'''DATABASES = {
        'USER': 'admin',
        'PASSWORD': 'admin1234',
        'HOST': 'se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {'ssl': False}
    
}'''

HOST='se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com'
USERNAME='admin'
PASSWORD='suma1234'
DB='SIGNUP'

#mysql = MySQL(app)

'''@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
		cur=conn.cursor()
		cur.execute('SELECT * FROM signup WHERE username = % s AND password = % s', (username, password, ))
		account = cur.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['id'] = account[0]
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))'''



'''@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
		cur=conn.cursor()
		cur.execute('SELECT * FROM signin WHERE username = % s AND password = % s', (email, password, ))
		account = cur.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['id'] = account[0]
			session['email'] = account[5]
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))'''

@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'departmentname' in request.form and 'clientname' in request.form and 'email' in request.form and 'password' in request.form :
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		departmentname=request.form['departmentname']
		clientname=request.form['clientname']
		email = request.form['email']
		password=request.form['password']
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
		cur=conn.cursor()
		#cur.execute('INSERT INTO signin VALUES (NULL, % s, % s, % s,% s, % s, % s)', (firstname,lastname,departmentname,clientname ,email, password, ))

		#cur.execute('SELECT * FROM signin WHERE email = % s and password=%s', (email,password, ))
		cur.execute('SELECT * FROM signin WHERE email = % s ', (email, ))
		account = cur.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', password):
			msg = 'Username must contain only characters and numbers !'
		elif not firstname or not lastname or not departmentname or not clientname or not email or not password:
			msg = 'Please fill out the form !'
		else:
			cur.execute('INSERT INTO signin VALUES (NULL, % s, % s, % s,% s, % s, % s)', (firstname,lastname,departmentname,clientname ,email, password, ))
			conn.commit()
			conn.close()
			msg = 'You have successfully registered !'
	#elif request.method == 'POST':
	#	msg = 'Please fill out the form !
	return render_template('register.html', msg = msg)

@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']
		#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
		cur=conn.cursor()
		cur.execute('SELECT * FROM signin WHERE email = % s AND password = % s', (email, password, ))
		account = cur.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['id'] = account[0]
			session['email'] = account[5]
			msg = 'Logged in successfully !'
			return render_template('upload.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route("/update", methods =['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'email' in request.form and 'password' in request.form :
			email = request.form['email']
			password = request.form['password']
			conn=pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,db=DB)
			cur=conn.cursor()
			cur.execute('SELECT * FROM signin WHERE email = % s', (email, ))
			'''account = cur.fetchone()
			if account:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', password):
				msg = 'name must contain only characters and numbers !'
			else:'''
			#cur.execute('UPDATE signin SET password =% s WHERE email =% s', ( password, (session['email'], ), ))
			cur.execute('UPDATE signin SET password =% s WHERE email =% s', ( password, (email, ), ))

			conn.commit()
			conn.close()
			msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg = msg)
	return redirect(url_for('login'))


s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
BUCKET_NAME='sepocbucket'

@app.route('/upload',methods=['post'])
def upload():
	if request.method == 'POST':
		img = request.files['file']
		if img:
				filename = secure_filename(img.filename)
				img.save(filename)
				s3.upload_file(
					Bucket = BUCKET_NAME,
					Filename=filename,
					Key = filename
				)
				msg = "Upload Done ! "
	
	
	return render_template("table.html",msg=msg)

@app.route('/tablenames',methods=['post','get'])
def tablenames():
	if request.method=='GET':
		mydb = mysql.connector.connect(
			host="se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com",
			user="admin",
			password="suma1234",
			database="SIGNUP"
		)
		
		mycursor = mydb.cursor()
		
		#mycursor.execute("Show tables;")
		mycursor.execute("SELECT table_name FROM information_schema.tables;")
		myresult = mycursor.fetchall()
		print(myresult)
	return render_template('table.html',myresult=myresult)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)
