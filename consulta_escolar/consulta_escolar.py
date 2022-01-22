#instalar biblioteca
#pip install mysql-connector-python

from multiprocessing import connection
from sqlite3 import Cursor, connect
from tkinter import _Cursor
import mysql.connector
from mysql.connector import Error
import pandas as pd

# criar a conexão
def create_server_connection (host_name, user_name, user_pasword):
    connection = None
    try:
        connection = mysql.connector.connect (host = host_name,user = user_name,passwd = user_pasword)
            
        print ("MySQL Database connection sucessful")
    except Error as err:
        print ("Error:'{err}'")
    return connection
    #TODO melhorar testes de conexão


#criar banco de dados
def create_database(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created sucessfully")
    except Error as err:
        print ("Error: '{err}'")


#Conectar com o banco de dados
def creat_db_connection(host_name, user_name, user_pasword, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host = host_name,user = user_name,passwd = user_pasword,database = db_name)
        print("MySQL Database connection successful")
    except Error as err:
        print("'Error: '{err}'")
    return connection

# Realizando a leitura
def read_query(connention, query):
    cursor - connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print("Error:'{err}'")

#para as consultas:
q1 = """
SELECT *
FROM User;
"""
connection = creat_db_connection("localhost", "root", pw,db)
results = read_query(connention, q1)

for result in results:
    print(result)
    
#formatando a lista de saída em um data frame 
from_db = []

for result in results:
    result = list(result)
    from_db.append(result)
    
columns = ["curso_id", "nome_curso","nome_cliente"]
df = pd.DataFrame(from_db, columns = columns)