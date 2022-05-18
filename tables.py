import mysql.connector
 
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
 
'''for x in myresult:
    print(x)'''