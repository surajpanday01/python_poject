import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Abcd1234@", database="LearnCoding")

db_cursor=mydb.cursor()

db_cursor.execute("select * from Emp" )

for db_data in db_cursor.fetchall():

    print(db_data)

  

db_select=db_cursor.fetchall()

print(db_select)