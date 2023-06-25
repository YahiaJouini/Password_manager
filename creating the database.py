import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS password_database")
if mycursor.rowcount>0:
    print("Database is successfully created")
else:
    print("Dadabase already exists")