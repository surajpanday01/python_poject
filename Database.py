import mysql.connector as MyConn

mydb=MyConn.connect(host="localhost",user="root",password="Abcd1234@")

db_cursor=mydb.cursor()

db_cursor.execute("create database LearnCoding")

print("Database Created!!")