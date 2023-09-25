import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Abcd1234@")

print(mydb, "connection established....")