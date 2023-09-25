import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Abcd1234@", database="LearnCoding")

db_cursor=mydb.cursor()

db_Updatedata="update Emp set roll=%s where Ename=%s"

db_value=(50,"Rohit")

db_cursor.execute(db_Updatedata,db_value)

mydb.commit()

print(db_cursor.rowcount,"Data Updated!!")
