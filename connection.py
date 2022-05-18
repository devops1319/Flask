import cx_Oracle
conn=cx_Oracle.connect(user="hr", password="welcome",
                               dsn="localhost/orclpdb1")
print(conn.version)
#cursor=conn.cursor()