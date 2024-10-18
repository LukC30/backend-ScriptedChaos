import mysql.connector
from flask import jsonify
import mysql.connector.cursor


class Database():
    user = ""
    password = ""
    host = ""
    db = ""

    def __init__(self, user, password, host, database):
        
        db_config = {
            self.user : user,
            self.password : password,
            self.host : host,
            self.db : database
        }
        try:
            db = mysql.connector.connect(db_config)
        except Exception as e:
            return jsonify({f"message": e})
        
        self.cursor = db.cursor()
        
        return 
    def insertCommand(self, fields, table, values):
        self.command = f"Insert into {table}({fields}) values({values})"
        return self.command
        
    def insertDatabase(self, fields, table, values, runTime):
        for i in runTime:
            try:
                self.cursor.execute(self.insertCommand(fields, table, values))
            except Exception as e:
                return jsonify({"message" : f"Erro no cadastro: {e}"})
        self.cursor.close()

        return jsonify({"message": f"cadastro feito com sucesso, {str(runTime)} cadastros feitos"})


        
    



