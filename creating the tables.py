import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='password_database'
)
mycursor=mydb.cursor()
mycursor.execute("create table information (username varchar (50),email varchar (50),password varchar (50), encrypt_key varchar (150),primary key(username,email))")