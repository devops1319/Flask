# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import re


app = Flask(__name__)


app.secret_key = 'your secret key'


'''app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'geekprofile'''

HOST='se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com'
USERNAME='admin'
PASSWORD='suma1234'
DB='SIGNUP'



@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        conn = pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DB)
        cur=conn.cursor()
        cur.execute('SELECT * FROM userdetails WHERE email = % s AND password = % s', (email, password, ))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
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
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'departmentname' in request.form and 'clientname' in request.form and 'email' in request.form and 'password' in request.form and 'postalcode' in request.form :
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        departmentname = request.form['departmentname']
        clientname = request.form['clientname']
        email = request.form['email']
        password = request.form['password']
        conn = pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DB)
        cur=conn.cursor()
        cur.execute('SELECT * FROM userdetails WHERE email = % s', (email, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', password):
            msg = 'password must contain only characters and numbers !'
        else:
            cur.execute('INSERT INTO userdetails VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (firstname,lastname,departmentname,clientname,email,password, ))
            conn.commit()
            #pymysql.connect.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)


@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("index.html")
	return redirect(url_for('login'))


@app.route("/display")
def display():
    if 'loggedin' in session:
        conn = pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DB)
        cur=conn.cursor()
        cur.execute('SELECT * FROM userdetails WHERE id = % s', (session['id'], ))
        account = cur.fetchone()	
        return render_template("display.html", account = account)
    return redirect(url_for('login'))

'''@app.route("/update", methods =['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			organisation = request.form['organisation']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']	
			postalcode = request.form['postalcode']
			conn = pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DB)
            cur=conn.cursor()
			cur.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
			account = cur.fetchone()
			if account:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'name must contain only characters and numbers !'
			else:
				cur.execute('UPDATE accounts SET username =% s, password =% s, email =% s, organisation =% s, address =% s, city =% s, state =% s, country =% s, postalcode =% s WHERE id =% s', (username, password, email, organisation, address, city, state, country, postalcode, (session['id'], ), ))
				mysql.connection.commit()
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg = msg)
	return redirect(url_for('login'))'''

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"))
