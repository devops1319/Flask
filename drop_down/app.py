
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/test', methods=['POST', 'GET'])
def test():
    mydb = mysql.connector.connect(
        host="se-poc.cwnyovbkqb1w.us-west-2.rds.amazonaws.com",
        user="admin",
        password="suma1234",
        database="SIGNUP"
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute("Show tables;")
    #mycursor.execute("SELECT table_name FROM information_schema.tables;")

    
    myresult = mycursor.fetchall()
    print(myresult)
    '''def test():
        if request.method == 'POST':
            print(request.form.get('age'))'''
    return render_template("test.html")


if __name__=='__main__':
    app.run(debug=True)
