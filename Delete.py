import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Abcd1234@", database="LearnCoding")

db_cursor=mydb.cursor()

db_deleteData="delete from  Emp where  Ename=%s"

db_value=("Rohit",)

db_cursor.execute(db_deleteData,db_value)

mydb.commit()

print(db_cursor.rowcount,"Record Deleted.")