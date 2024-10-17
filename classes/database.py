import mysql.connector
from flask import jsonify
import mysql.connector.cursor
import requests



class Database:
    def __init__(self, user, password, host, database):
        db_config = {
            self.user : user,
            self.password : password,
            self.host : host,
            self.database : database
        }
        try:
            db = mysql.connector.connect(db_config)
        except Exception as e:
            return jsonify({"message":f"{e}"})
        
        self.cursor = mysql.connector.cursor()
        
    def insert(self, data, table):
        self.command = f"Insert into {table}"
        return 
    def insertWithWhere()
        

    def execute(query)


        
    



