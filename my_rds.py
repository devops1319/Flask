import pandas as pd
import pymysql
host="poc-rds.cwnyovbkqb1w.us-west-2.rds.amazonaws.com"
port=3306
dbname="poc-rds"
user="admin"
password="admin1234"

'''connection = pymysql.connect('poc-rds.cwnyovbkqb1w.us-west-2.rds.amazonaws.com','admin','suma1234')
cursor=connection.cursor()'''
db = pymysql.connect(host='poc-rds.cwnyovbkqb1w.us-west-2.rds.amazonaws.com',user='admin',password='suma1234',database = 'poc-rds', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
'''cursor=connection.cursor()
cursor.execute("""CREATE TABLE passengers(
name varchar(10))""")'''