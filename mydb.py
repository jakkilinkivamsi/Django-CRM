#Install Mysql on your computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python


import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ismav_3182'
)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a databse
cursorObject.execute("CREATE DATABASE project")

print("All Done!..")


