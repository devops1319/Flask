from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def home():
    return 'Welcome to the world'

@app.route('/add')
def add():
    a=10
    b=20
    return str(a+b)

if __name__=='__main':
    app.run(debug=True)