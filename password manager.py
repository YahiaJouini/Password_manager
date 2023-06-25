import mysql.connector
from user import user_info
from random import randint


#connecting to the database
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='password_database'
)
mycursor=db.cursor()



#checking the validity of the username
def valid(username):
    for char in username:
        if char.isnumeric() or not ("A"<=char.upper()<="Z" or char==" "):
            return  False
    return True

#encrypting the password
def encrypt(string):
    key=''
    i=0
    while i<126:
        tmp=randint(0,126)
        if key.find(chr(tmp))==-1 and tmp!=10:
            key+=chr(tmp)
            i+=1
    characters=""
    for i in range(127):
        characters+=chr(i)
    crypted_pass=''
    for i in range(len(string)):
        position=characters.find(string[i])
        crypted_pass+=key[position]
    return crypted_pass,key

#decrypting the password
def decrypt_password(str1,str2):
    characters=""
    for i in range(127):
        characters+=chr(i)
    result=""
    for i in range(len(str1)):
        position=str2.find(str1[i])
        result+=characters[position]
    return result

#chosing whether to insert or to view a password
print("Press 'I' to insert a new account")
print("press 'V' to view an already existing account")
while True:
    choice=input("Your response : ")
    if choice.upper() in ('V','I'):
        break
    else:
        print("Press 'I' or 'V' !")
print("="*80)
print('')


#inserting a new account
if choice.upper()=="I":
    while True:
        username = input("Enter your username : ")
        if valid(username):
            break
    user_info.username = username
    while True:
        email = input("Enter your email :  ")
        if email.find('@')>0 and email.count('@') == 1 and email.endswith('.com') and email.find(' ')==-1:
            break
    user_info.email = email
    password = input("Enter your password : ")
    user_info.password = password
    print("="*80)
    print('')
    req = "select password,encrypt_key from information where username=%s and email=%s"
    mycursor.execute(req, (user_info.username, user_info.email))
    result = mycursor.fetchall()
    if len(result) == 0:
        crypted_password,key=encrypt(user_info.password)
        mycursor.execute("insert into information values(%s,%s,%s,%s)",(user_info.username,user_info.email,crypted_password,key))
        db.commit()
        if mycursor.rowcount>0:
            print("The informations are successfully inserted!")
        else:
            print(mysql.connector.errors)
    else:
        print('The informations you provided are already saved')


#viewing an already existing password
else:
    username=input("Enter your username : ")
    email=input("Enter your email :  ")
    req="select password,encrypt_key from information where username=%s and email=%s"
    mycursor.execute(req,(username,email))
    result=mycursor.fetchall()
    if len(result)==0:
        print('Unavailable user')
    else:
        password=decrypt_password(result[0][0],result[0][1])
        print(f"The password is {password}")